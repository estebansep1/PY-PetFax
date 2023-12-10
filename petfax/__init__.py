# __init__.py
from flask import Flask
from .pet import bp as pet_bp

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, PetFax!'
    
    app.register_blueprint(pet_bp)

    return app
