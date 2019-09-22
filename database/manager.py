# Python core imports
import os

# Third-party imports
from orator import DatabaseManager
from orator import Model

# Importing local models
from database.models import posts
from database.models import drafts
from database.models import users
from database.models import notes


class Database:

    db = None
    config = {}

    Posts = None
    Drafts = None
    Users = None
    Notes = None

    # Config
    config = {}

    def __init__(self):
        # Bind Models to local variables
        self.Posts = posts
        self.Drafts = drafts
        self.Users = users
        self.Notes = notes

        # Set config
        self.config = {
            'mysql': {
                'driver': 'mysql',
                'host': os.getenv('DB_HOST'),
                'database': os.getenv('DB_NAME'),
                'user': os.getenv('DB_USER'),
                'password': os.getenv('DB_PASSWORD'),
                'prefix': ''
            }
        }

        # Create database from config
        self.db = DatabaseManager(self.config)

        # Auto-resolve connection
        Model.set_connection_resolver(self.db)


# Create public instance
db = Database()
