from flask import Blueprint, request, make_response, jsonify
import datetime
from flask.views import MethodView
from api.models import Meal, MealDetail
from api.helpers import validate_request
from .unique_id import PushID
from ..errors import response_object

class UserBookMealApi(MethodView):
    """
    User book meal Resource
    """
    @validate_request((str, 'MealPeriod', 'PostedBy'))
    def post(self):
        post_data = request.get_json()
        meal_book = Meal.query.filter_by(username=post_data.get('PostedBy'),meal_period=post_data.get('MealPeriod'),date=post_data.get('MealDate')).first()
        mealList = post_data.get('MealDetails')
        if meal_book:
            return response_object('fail', 'You have already booked a meal for {}'.format(meal_book.meal_period), 202)
        else:
            try:
                mealId = PushID().next_id()
                meal = Meal(
                    _id = mealId,
                    date = post_data.get('MealDate'),
                    meal_period=post_data.get('MealPeriod'),
                    username=post_data.get('PostedBy'),
                )

                #insert the meal
                meal.save()
                for meal in mealList:
                    mealDetail = MealDetail(
                        _id = PushID().next_id(),
                        meal_id= mealId,
                        menu_detail_id=meal['MealTypeId']
                    )
                responseObject = {
                    'status': 'success',
                    'message': 'You have successfuly booked a meal'
                }
                return make_response(jsonify(response_object)), 201
            except Exception as e:
                print(e)
                return response_object('fail', 'An error occured while processing your request. Please try again.', 401)
