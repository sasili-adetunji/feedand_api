from flask import Blueprint, request, make_response, jsonify
import datetime
from flask.views import MethodView
from api.models import Caterer, Menu
from api.helpers import validate_request, hash_pwd
from .unique_id import PushID
from ..errors import response_object


class MenuAPI(MethodView):
    """
    Menu Creating Resource
    """
    # @validate_request((str, "email", "password"))
    def post(self):
        # get the post data
        post_data = request.get_json()
        #print (post_data)
        # check if user already exists
        caterer = Caterer.query.filter_by(_id=post_data.get('catererId')).first()
        if not caterer:
            return response_object('fail', 'This caterer does not exist', 400)
        else:
            try:
                menu = Menu(
                    _id = PushID().next_id(),
                    meal_period=post_data.get('mealPeriod'),
                    caterer_id=post_data.get('catererId'),
                    date=post_data.get('date')
                )

                # insert the user
                menu.save()
                responseObject = {
                    'status': 'success',
                    'data': menu.serialize(),
                    'message': 'Menu successfully created',
                }
                return make_response(jsonify(responseObject)), 201
            except Exception as e:
                print(e)
                return response_object('fail', 'Some error occurred. Please try again.', 401)
