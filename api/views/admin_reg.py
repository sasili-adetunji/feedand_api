from flask import Blueprint, request, make_response, jsonify
import datetime
from flask.views import MethodView
from api.models import User
from api.helpers import validate_request, hash_pwd
from .unique_id import PushID
from ..errors import response_object


class AdminRegisterAPI(MethodView):
    """
    User Registration Resource
    """
    @validate_request((str, "email", "password"))
    def post(self):
        # get the post data
        post_data = request.get_json()
        # check if user already exists
        user = User.query.filter_by(email=post_data.get('email')).first()
        if user:
            return response_object('fail', 'This account already exists and active', 202)
        else:
            try:
                user = User(
                    user_id = PushID().next_id(),
                    email=post_data.get('email'),
                    password=post_data.get('password'),
                )

                # insert the user
                user.save()
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully registered. Kindly log in to register',
                }
                return make_response(jsonify(responseObject)), 201
            except Exception as e:
                print(e)
                return response_object('fail', 'Some error occurred. Please try again.', 401)
