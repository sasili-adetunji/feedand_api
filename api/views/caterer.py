from flask import Blueprint, request, make_response, jsonify
import datetime
from flask.views import MethodView
from api.models import Caterer, User
from api.helpers import validate_request, hash_pwd
from .unique_id import PushID
from ..errors import response_object


class CatererAPI(MethodView):
    """
    Create Caterer Resource
    """
    @validate_request((str, "business_name", "contact_person", "email", "phone_number", "username", "password"))
    def post(self):
        # get the post data
        post_data = request.get_json()
        # check if user already exists
        business_name = Caterer.query.filter_by(business_name=post_data.get('business_name')).first()
        if business_name:
            return response_object('fail', 'This business_name already exists', 202)
        else:
            try:
                caterer = Caterer(
                    caterer_id = PushID().next_id(),
                    business_name=post_data.get('business_name'),
                    contact_person=post_data.get('contact_person'),
                    email=post_data.get('email'),
                    phone_number=post_data.get('phone_number'),
                    username=post_data.get('username'),
                    password=post_data.get('password'),
                )

                # insert the user
                caterer.save()
                responseObject = {
                    'status': 'success',
                    'message': 'Caterer successfully registered.',
                }
                return make_response(jsonify(responseObject)), 201
            except Exception as e:
                print(e)
                return response_object('fail', 'Some error occurred. Please try again.', 401)

    def get(self):
        # get the token
        auth_header = request.headers.get('Authorization')

        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                return response_object('fail', 'Bearer token malformed.', 401)
        else:
            auth_token = ''

        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                caterer = Caterer.query.all()
                result = [{"business_name": i.business_name, "caterer_id": i.caterer_id, "contact_person": i.contact_person,
                "email": i.email, "phone_number": i.phone_number, "username": i.username, "status": i.isActive } for i in caterer]
                if not caterer:
                    responseObject = {
                        'status': 'fail',
                        'message': 'No Caterer added yet'
                    }
                    return make_response(jsonify(responseObject)), 404
                else:
                    responseObject = {
                        'status': 'success',
                        'data': {
                            'records': result,
                        }
                    }
                    return make_response(jsonify(responseObject)), 200
            return response_object('fail', resp, 401)
        else:
            return response_object('fail', 'Provide a valid token.', 401)