from flask_restful import Resource
from app import app

class User(Resource):
    def get(self):
        return "Zeb ur Rehman"