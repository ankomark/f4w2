#!/usr/bin/env python3
from flask import Flask
from routes.episode_routes import episode_routes
from routes.guest_routes import guest_routes
from routes.appearance_routes import appearance_routes
from db import db
from flask_migrate import Migrate

# Initializing the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///late_show.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Registering the blueprints for routes
app.register_blueprint(episode_routes)
app.register_blueprint(guest_routes)
app.register_blueprint(appearance_routes)

@app.route('/')
def home():
    """Health check endpoint to confirm the API is operational."""
    return "Late Show API is running!", 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
