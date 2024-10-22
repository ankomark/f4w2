#!/usr/bin/env python3
from flask import Blueprint, request, jsonify
from models.episode import Episode
from models.appearance import Appearance
from db import db

# Creating a blueprint for episode routes
episode_routes = Blueprint('episodes', __name__)

@episode_routes.route('/episodes', methods=['GET'])
def get_episodes():
    """Retrieve a list of all episodes."""
    episodes = Episode.query.all()
    return jsonify([{
        "id": episode.id,
        "date": episode.date,
        "number": episode.number
    } for episode in episodes]), 200

@episode_routes.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    """Retrieve a specific episode by ID."""
    episode = Episode.query.get(id)
    if episode:
        appearances = Appearance.query.filter_by(episode_id=episode.id).all()
        return jsonify({
            "id": episode.id,
            "date": episode.date,
            "number": episode.number,
            "appearances": [{
                "episode_id": appearance.episode_id,
                "guest": {
                    "id": appearance.guest.id,
                    "name": appearance.guest.name,
                    "occupation": appearance.guest.occupation
                },
                "guest_id": appearance.guest_id,
                "id": appearance.id,
                "rating": appearance.rating
            } for appearance in appearances]
        }), 200
    
    return jsonify({"error": "Episode not found"}), 404

@episode_routes.route('/episodes', methods=['POST'])
def create_episode():
    """Create a new episode."""
    data = request.json
    new_episode = Episode(date=data['date'], number=data['number'])
    db.session.add(new_episode)
    db.session.commit()
    return jsonify(new_episode.to_dict()), 201

@episode_routes.route('/episodes/<int:id>', methods=['PUT'])
def update_episode(id):
    """Update an existing episode."""
    episode = Episode.query.get(id)
    if episode:
        data = request.json
        episode.date = data['date']
        episode.number = data['number']
        db.session.commit()
        return jsonify(episode.to_dict()), 200
    return jsonify({"error": "Episode not found"}), 404

@episode_routes.route('/episodes/<int:id>', methods=['DELETE'])
def delete_episode(id):
    """Delete an episode by ID."""
    episode = Episode.query.get(id)
    if episode:
        db.session.delete(episode)
        db.session.commit()
        return jsonify({"message": "Episode deleted"}), 204
    return jsonify({"error": "Episode not found"}), 404
