from flask import Blueprint, request, make_response, jsonify
from datetime import datetime
from flask.views import MethodView
from api.models import User



class DummyApi(MethodView):
    """
    User Resource
    """
    def get(self):
        # get the auth token
        return "Welcome to our world"
