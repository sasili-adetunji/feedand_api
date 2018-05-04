from flask import Blueprint

from api.views.dummy import DummyApi
from api.views.admin_reg import AdminRegisterAPI
from api.views.admin_login import AdminLoginAPI
from api.views.user_book_meal import UserBookMealApi

dummy_blueprint = Blueprint('dummy', __name__)
admin_reg_blueprint = Blueprint('admin_reg', __name__)
admin_login_blueprint = Blueprint('admin_login', __name__)
user_book_meal_blueprint = Blueprint('user_book_meal', __name__)


dummy_view = DummyApi.as_view('dummy')
admin_reg_view = AdminRegisterAPI.as_view('admin_reg')
admin_login_view = AdminLoginAPI.as_view('admin_login')
user_book_meal_view = UserBookMealApi.as_view('user_book_meal')

dummy_blueprint.add_url_rule(
    '/dummy',
    view_func=dummy_view,
    methods=['GET']
)

admin_reg_blueprint.add_url_rule(
    '/auth/admin/register',
    view_func=admin_reg_view,
    methods=['POST']
)

admin_login_blueprint.add_url_rule(
    '/auth/admin/login',
    view_func=admin_login_view,
    methods=['POST']
)

user_book_meal_blueprint.add_url_rule(
    '/api/andelans/bookmeal',
    view_func=user_book_meal_view,
    methods=['POST']
)