from flask import Flask
from flask_migrate import Migrate
from decouple import config

def create_app():
    app = Flask(__name__)

    # Load configuration from .env file
    app.config['SQLALCHEMY_DATABASE_URI'] = config('SQLALCHEMY_DATABASE_URI', default='')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    # index route
    @app.route('/')
    def index():
        return 'Hello, PetFax!'

    # register pet blueprint
    from . import pet
    app.register_blueprint(pet.pet_bp)

    # register fact blueprint
    from . import fact
    app.register_blueprint(fact.bp)

    # return the app
    return app