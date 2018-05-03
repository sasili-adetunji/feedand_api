from flask import Blueprint

from api.views.dummy import DummyApi
from api.views.admin_reg import AdminRegisterAPI

dummy_blueprint = Blueprint('dummy', __name__)
admin_reg_blueprint = Blueprint('admin_reg', __name__)

dummy_view = DummyApi.as_view('dummy')
admin_reg_view = AdminRegisterAPI.as_view('admin_reg')

dummy_blueprint.add_url_rule(
    '/dummy',
    view_func=dummy_view,
    methods=['GET']
)

admin_reg_blueprint.add_url_rule(
    '/auth/admin',
    view_func=admin_reg_view,
    methods=['POST']
)
