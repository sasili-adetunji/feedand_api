from flask import Blueprint

from api.views.dummy import DummyApi
from api.views.admin_reg import AdminRegisterAPI
from api.views.admin_login import AdminLoginAPI
<<<<<<< HEAD
from api.views.user_book_meal import UserBookMealApi
from api.views.menu import MenuAPI
from api.views.menu_details import MenuDetailAPI
from api.views.feedback import FeedBackAPI
=======
from api.views.caterer import CatererAPI
>>>>>>> add caterer endpoints

dummy_blueprint = Blueprint('dummy', __name__)
admin_reg_blueprint = Blueprint('admin_reg', __name__)
admin_login_blueprint = Blueprint('admin_login', __name__)
<<<<<<< HEAD
user_book_meal_blueprint = Blueprint('user_book_meal', __name__)

menu_blueprint = Blueprint('menu', __name__)
menu_item_blueprint = Blueprint('menu_details', __name__)
feedback_blueprint = Blueprint('feedback', __name__)
=======
caterer_blueprint = Blueprint('caterer', __name__)
>>>>>>> add caterer endpoints

dummy_view = DummyApi.as_view('dummy')
admin_reg_view = AdminRegisterAPI.as_view('admin_reg')
admin_login_view = AdminLoginAPI.as_view('admin_login')
<<<<<<< HEAD
user_book_meal_view = UserBookMealApi.as_view('user_book_meal')
menu_view = MenuAPI.as_view('menu')
menu_details_view = MenuDetailAPI.as_view('menu_details')
feedback_view = FeedBackAPI.as_view('feedback')

=======
caterer_view = CatererAPI.as_view('caterer')
>>>>>>> add caterer endpoints

dummy_blueprint.add_url_rule(
    '/dummy',
    view_func=dummy_view,
    methods=['GET']
)

menu_blueprint.add_url_rule(
    '/api/caterer/postmenu',
    view_func=menu_view,
    methods=['POST']
)

menu_item_blueprint.add_url_rule(
    '/api/caterer/postmenudetails',
    view_func=menu_details_view,
    methods=['POST']
)

feedback_blueprint.add_url_rule(
    '/api/andelans/postfeedback',
    view_func=feedback_view,
    methods=['POST']
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

<<<<<<< HEAD
user_book_meal_blueprint.add_url_rule(
    '/api/andelans/bookmeal',
    view_func=user_book_meal_view,
    methods=['POST']
=======
caterer_blueprint.add_url_rule(
    '/admin/caterer',
    view_func=caterer_view,
    methods=['POST', 'GET']
>>>>>>> add caterer endpoints
)