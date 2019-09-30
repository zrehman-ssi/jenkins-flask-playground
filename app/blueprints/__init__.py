from flask import Blueprint
from flask_restful import Api
from app.controllers.users_controller import User

blueprint  = Blueprint("api", __name__)
api = Api(blueprint)
api.add_resource(User, '/', '/')