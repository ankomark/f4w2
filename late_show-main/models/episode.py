#!/usr/bin/env python3
from db import db

class Episode(db.Model):
    """class that defines an episode of the late show."""

    __tablename__ = 'episodes'

    # Defining the columns in the episodes table
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    # Define the relationship to appearances, allowing automatic deletion of related appearances
    appearances = db.relationship('Appearance', back_populates='episode', cascade='all, delete-orphan')

    def to_dict(self):
        """Converts episode instance to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'date': self.date,
            'number': self.number,
            'appearances': [appearance.to_dict() for appearance in self.appearances]
        }

    @staticmethod
    def check_duplicate(number):
        """checks if an episode already exists in the database"""
        existing_episode = Episode.query.filter_by(number = number).first()
        if existing_episode:
            raise ValueError("That episode already exists.")