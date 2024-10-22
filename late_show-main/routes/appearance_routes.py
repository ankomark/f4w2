#!/usr/bin/env python3
from flask import Blueprint, request, jsonify
from models.appearance import Appearance
from models.episode import Episode
from models.guest import Guest
from db import db

# Creating a blueprint for appearance routes
appearance_routes = Blueprint('appearances', __name__)

@appearance_routes.route('/appearances', methods=['GET'])
def get_appearances():
    """Retrieve a list of all appearances."""
    appearances = Appearance.query.all()
    return jsonify([appearance.to_dict() for appearance in appearances]), 200

@appearance_routes.route('/appearances/<int:id>', methods=['GET'])
def get_appearance(id):
    """Retrieve a specific appearance by ID."""
    appearance = Appearance.query.get(id)
    if appearance:
        return jsonify(appearance.to_dict()), 200
    return jsonify({"message": "Appearance not found"}), 404

@appearance_routes.route('/appearances', methods=['POST'])
def create_appearance():
    """Create a new appearance."""
    data = request.json

    # Validate required fields
    if not all(key in data for key in ("rating", "episode_id", "guest_id")):
        return jsonify({"errors": ["validation errors"]}), 400

    try:
        # Validate the rating
        Appearance.validate_rating(data['rating'])

        # Checking if an episode exists
        episode = Episode.query.get(data['episode_id'])
        guest = Guest.query.get(data['guest_id'])
        if not episode or not guest:
            return jsonify({"errors": ["Episode or Guest not found"]}), 404

        existing_appearance = Appearance.query.filter_by(episode_id=data['episode_id'], guest_id=data['guest_id']).first()
        if existing_appearance:
            return jsonify({"error": ["Duplicate appearance: This guest is already associated with this episode"]}), 400

        # Create new appearance instance
        new_appearance = Appearance(rating=data['rating'], episode_id=data['episode_id'], guest_id=data['guest_id'])  
        db.session.add(new_appearance)
        db.session.commit()

        # Prepare response data
        response_data = {
            "id": new_appearance.id,
            "rating": new_appearance.rating,
            "guest_id": new_appearance.guest_id,
            "episode_id": new_appearance.episode_id,
            "episode": {
                "date": episode.date,
                "id": episode.id,
                "number": episode.number
            },
            "guest": {
                "id": guest.id,
                "name": guest.name,
                "occupation": guest.occupation
            }
        }
        return jsonify(response_data), 201

    except ValueError as ve:
        return jsonify({"errors": [str(ve)]}), 400
    except Exception as e:
        return jsonify({"errors": ["An error occurred"]}), 500

@appearance_routes.route('/appearances/<int:id>', methods=['PUT'])
def update_appearance(id):
    """Update an existing appearance."""
    appearance = Appearance.query.get(id)
    if appearance:
        data = request.json

        # Validate the rating
        Appearance.validate_rating(data['rating'])
        appearance.rating = data['rating']
        appearance.episode_id = data['episode_id']
        appearance.guest_id = data['guest_id']
        db.session.commit()
        return jsonify(appearance.to_dict()), 200
    return jsonify({"message": "Appearance not found"}), 404

@appearance_routes.route('/appearances/<int:id>', methods=['DELETE'])
def delete_appearance(id):
    """Delete an appearance by ID."""
    appearance = Appearance.query.get(id)
    if appearance:
        db.session.delete(appearance)
        db.session.commit()
        return jsonify({"message": "Appearance deleted"}), 204
    return jsonify({"message": "Appearance not found"}), 404
