from flask import Blueprint, request, make_response, jsonify
import datetime
from flask.views import MethodView
from api.models import FeedBack
from api.models import Meal
from api.helpers import validate_request, hash_pwd
from .unique_id import PushID
from ..errors import response_object


class FeedBackAPI(MethodView):
    """
    Menu Creating Resource
    """
    # @validate_request((str, "email", "password"))
    def post(self):
        # get the post data
        post_data = request.get_json()
        # check if menu exists
        meal = Meal.query.filter_by(_id=post_data.get('meal_id')).first()
        if not meal:
            return response_object('fail', 'This meal does not exist', 400)
        else:
            try:
                feedback = FeedBack(
                    _id = PushID().next_id(),
                    meal_id=post_data.get('menuId'),
                    comment=post_data.get('comment'),
                    comment_by=post_data.get('commentBy'),
                    rating=post_data.get('rating')
                )

                # insert the user
                feedback.save()
                responseObject = {
                    'status': 'success',
                    'message': 'Feed back successfully added',
                }
                return make_response(jsonify(responseObject)), 201
            except Exception as e:
                print(e)
                return response_object('fail', 'Some error occurred. Please try again.', 401)
