from flask import Blueprint, request, make_response, jsonify
import datetime
from flask.views import MethodView
from api.models import User
from api.helpers import validate_request, hash_pwd
from .unique_id import PushID
from ..errors import response_object
from api import bcrypt


class AdminLoginAPI(MethodView):
    """
    User Login Resource
    """

    @validate_request((str, "email", "password"))
    def post(self):
        # get the post data
        post_data = request.get_json()
        try:
            # fetch the user data
            user = User.query.filter_by(
                email=post_data.get('email')
            ).first()
            if user:
                if bcrypt.check_password_hash(user.password, post_data.get('password')):
                    auth_token = user.encode_auth_token(user.user_id)
                    responseObject = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'auth_token': auth_token.decode()
                    }
                    return make_response(jsonify(responseObject)), 200
                return response_object('fail', 'Login credentials is incorrect.', 404)
            else:
                return response_object('fail', 'Login credentials is incorrect.', 404)
        except Exception as e:
            print(e)
            return response_object('fail', 'Try again', 500)