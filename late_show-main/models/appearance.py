#!/usr/bin/env python3
from db import db

class Appearance(db.Model):
    """Model representing a guest appearance on an episode."""

    __tablename__ = 'appearances'

    # Defining the columns in the appearances table
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)

    # Defining relationships
    episode = db.relationship('Episode', back_populates='appearances')
    guest = db.relationship('Guest', back_populates='appearances')

    def to_dict(self):
        """Convert the appearance instance to a dictionary format for JSON serialization."""
        return {
            'id': self.id,
            'rating': self.rating,
            'guest_id': self.guest_id,
            'episode_id': self.episode_id,
            'guest': self.guest.to_dict() if self.guest else None,
        }

    @classmethod
    def validate_rating(cls, rating):
        """Validate that the rating is between 1 and 5."""
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")
        
    @staticmethod
    def check_duplicate(guest_id, episode_id):
        """checks if a guest has already appeared in an episode"""
        existing_appearance = Appearance.query.filter_by(guest_id = guest_id, episode_id = episode_id).first()
        if existing_appearance:
            raise ValueError("{guest_id.name} already appeared in this episode{episode_id.number}.")
