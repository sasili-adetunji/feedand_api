from flask import Blueprint

from api.views.dummy import DummyApi
from api.views.admin_reg import AdminRegisterAPI
from api.views.admin_login import AdminLoginAPI

dummy_blueprint = Blueprint('dummy', __name__)
admin_reg_blueprint = Blueprint('admin_reg', __name__)
admin_login_blueprint = Blueprint('admin_login', __name__)


dummy_view = DummyApi.as_view('dummy')
admin_reg_view = AdminRegisterAPI.as_view('admin_reg')
admin_login_view = AdminLoginAPI.as_view('admin_login')

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
