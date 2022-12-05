from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("PG_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello():
        return "Hello petfax from the factory!"

    from.import pet    
    app.register_blueprint(pet.bp)

    from .import fact
    app.register_blueprint(fact.bp)


    return app    