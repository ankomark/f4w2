# *LATE SHOW*

## *Project Description*

The Late Show API models relationships between episodes, guests, and their appearances, allowing users to manage and query this data. The database stores information about each episode, guest, and appearance.

## *Project Structure*

```bash*

late_show/
│
├── app.py                                       # Main entry point for the Flask application
├── db.py                                        # Database setup and initialization
├── seed.py                                      # Seed data for the database
├── requirements.txt                             # List of dependencies
├── instance/                                    # Folder for database file
│   ├── late_show.db                             # SQLite database file
├── migrations/                                  # Folder for database migrations
│   ├── versions/                                # Folder for migration scripts
├── models/                                      # Folder for data models
│   ├── __init__.py                              # Empty init file for models package
│   ├── episode.py                               # Model for episodes
│   ├── guest.py                                 # Model for guests
│   ├── appearance.py                            # Model for appearances
├── routes/                                      # Folder for API routes
│   ├── __init__.py                              # Empty init file for routes package
│   ├── episode_routes.py                        # Routes for managing episodes
│   ├── guest_routes.py                          # Routes for managing guests
│   ├── appearance_routes.py                     # Routes for managing appearances
└── utils/                                       # Utility folder
|
└── challenge-4-lateshow.postman_collection.json # Postman collection for testing

```

## *Project Preview*

- ***`app.py`***
Main entry point for the Flask application, responsible for running the server

- ***`db.py`***
Handles the database setup and initialization using SQLAlchemy

- ***`seed.py`***
Populates the database with initial data for episodes, guests, and appearances

- ***`requirements.txt`***
Lists the dependencies required for the project, including Flask and SQLAlchemy

- ***instance/***
A directory for storing application-specific files like the SQLite database

- ***instance/`late_show.db`***
SQLite database file that holds all the data for the application

- ***migrations/***
Directory that manages database schema migrations

- ***migrations/versions/***
Contains versioned migration scripts that track schema changes over time

- ***models/***
Directory containing the data models for episodes, guests, and appearances

- ***models/`__init__.py`***
Initializes the models package for use within the application

- ***models/`episode.py`***
Defines the Episode model, representing TV show episodes in the database

- ***models/`guest.py`***
Defines the Guest model, representing individual guests in the database

- ***models/`appearance.py`***
Defines the Appearance model, linking episodes and guests in the database

- ***routes/***
Directory containing API route definitions for managing episodes, guests, and appearances

- ***routes/`episode_routes.py`***
Contains API routes for creating, retrieving, and managing episodes

- ***routes/`guest_routes.py`***
Contains API routes for creating, retrieving, and managing guests

- ***routes/`appearance_routes.py`***
Contains API routes for creating, retrieving, and managing appearances of guests on episodes

- ***utils/***
Directory for utility files, such as the Postman collection for testing the API

## Endpoints

### Guests

- `GET /guests`: Get all guests.
- `GET /guests/<id>`: Get a specific guest by ID.

### Episodes

- `GET /episodes`: Get all episodes.
- `GET /episodes/<id>`: Get a specific episode by ID.

### Appearances

- `POST /appearances`: Create a new `Appearance` that is associated with an existing `Episode` and `Guest`

#### NOTE

Ensure the body section of postman has a raw json structure as:

```bash
{
  "rating": 4,
  "episode_id": 6,
  "guest_id": 11
}
```

## Setup

- Clone the repository.
- Create environment **(optional)** with `pipenv install`, shell using `pipenv shell` 
- install dependencies with `pip install -r requirements.txt`.
- Create the database with:

```bash
flask db init
flask db migrate -m 'Initial Migration'
flask db upgrade
```

- Run `python seed.py` to seed the database.
- Start the app with `python app.py`.
- Use the URL link together with the API endpoints to run in your postman extension or app.
 For example: `GET http://127.0.0.1:5555/episodes/`
