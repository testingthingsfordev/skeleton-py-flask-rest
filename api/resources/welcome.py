from flask_restful import Resource
from flask import jsonify


class Welcome(Resource):
    def get(self):
        return jsonify({"data": "Welcome to python API!"})
