# import os

# from flask import Flask, Blueprint
# from flask_bcrypt import Bcrypt
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# app_settings = os.getenv(
#     'APP_SETTINGS',
#     'api.config.DevelopmentConfig'
# )
# app.config.from_object(app_settings)

# bcrypt = Bcrypt(app)
# db = SQLAlchemy(app)

# from api.blueprint import dummy_blueprint
# app.register_blueprint(dummy_blueprint)

