from flask import Blueprint, request, make_response, jsonify
import datetime
from flask.views import MethodView
from api.models import MenuDetail, Menu
from api.helpers import validate_request, hash_pwd
from .unique_id import PushID
from ..errors import response_object


class MenuDetailAPI(MethodView):
    """
    Menu Creating Resource
    """
    # @validate_request((str, "email", "password"))
    def post(self):
        # get the post data
        post_data = request.get_json()
        # check if menu exists
        menu = Menu.query.filter_by(_id=post_data.get('menuId')).first()
        if not menu:
            return response_object('fail', 'This menu does not exist', 400)
        else:
            try:
                menuDetails = MenuDetail(
                    _id = PushID().next_id(),
                    menu_id=post_data.get('menuId'),
                    menu_name=post_data.get('menuName'),
                    category_id=post_data.get('categoryId')
                )

                # insert the user
                menuDetails.save()
                responseObject = {
                    'status': 'success',
                    'data': menuDetails.serialize(),
                    'message': 'Menu items successfully created',
                }
                return make_response(jsonify(responseObject)), 201
            except Exception as e:
                print(e)
                return response_object('fail', 'Some error occurred. Please try again.', 401)
