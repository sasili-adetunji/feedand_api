from flask import Blueprint

from api.views.dummy import DummyApi
from api.views.admin_reg import AdminRegisterAPI
from api.views.admin_login import AdminLoginAPI
from api.views.menu import MenuAPI
from api.views.menu_details import MenuDetailAPI
from api.views.feedback import FeedBackAPI

dummy_blueprint = Blueprint('dummy', __name__)
admin_reg_blueprint = Blueprint('admin_reg', __name__)
admin_login_blueprint = Blueprint('admin_login', __name__)
menu_blueprint = Blueprint('menu', __name__)
menu_item_blueprint = Blueprint('menu_details', __name__)
feedback_blueprint = Blueprint('feedback', __name__)

dummy_view = DummyApi.as_view('dummy')
admin_reg_view = AdminRegisterAPI.as_view('admin_reg')
admin_login_view = AdminLoginAPI.as_view('admin_login')
menu_view = MenuAPI.as_view('menu')
menu_details_view = MenuDetailAPI.as_view('menu_details')
feedback_view = FeedBackAPI.as_view('feedback')


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
    view_func=menu_view,
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
