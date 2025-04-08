from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

if __name__ == '__main__':
    # Add the Flask-Frozen first with: pip install Frozen-Flask
    freezer.freeze()