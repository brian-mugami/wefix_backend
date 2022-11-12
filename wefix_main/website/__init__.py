import os
import redis
import secrets
from redis import Redis
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_smorest import Api
from flask_session import Session

from website.db import db

migrate = Migrate()
api = Api()
server_session = Session()
redis_user = Redis(host='redis', port=6379)
def create_app():
    load_dotenv(".env", verbose=True)
    app = Flask(__name__)
    db_pass = os.environ.get("DB_PASS")
    db_name = os.environ.get("DB_NAME")
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "wefix REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"  # for documentation purposes..http://localhost:7005{port no}/swagger-ui
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://postgres:{db_pass}@db/{db_name}'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SESSION_TYPE"] = "redis"
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_USE_SIGNER"] = True
    app.config["SESSION_REDIS"] = redis.from_url("redis://redis")
    app.secret_key = secrets.token_urlsafe(16)
    CORS(app)

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)
        api.init_app(app)
        server_session.init_app(app)
        #from .models import UserModel, WorkersModel, WorkerTypeModel, SeekersModel, ConnectionModel, LocationModel
        #db.create_all()

        from .auth import auth
        from .views import location
        api.register_blueprint(auth)
        api.register_blueprint(location)

    return app
