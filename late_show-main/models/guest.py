#!/usr/bin/env python3
from db import db

class Guest(db.Model):
    """Model representing a guest on the late show."""

    __tablename__ = 'guests' 

    # Defining the columns in the guests table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)

    # Define the relationship to appearances, allowing automatic deletion of related appearances
    appearances = db.relationship('Appearance', back_populates='guest', cascade='all, delete-orphan')

    def to_dict(self):
        """Convert the guest instance to a dictionary format for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'occupation': self.occupation
        }

    @staticmethod
    def check_duplicate(name):
        """checks if a duplicate guest name exists"""
        existing_guest = Guest.query.filter_by(name = name).first()
        if existing_guest:
            raise ValueError("The guest with that name exists.")