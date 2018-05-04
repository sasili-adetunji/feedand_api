import os

basedir = os.path.abspath(os.path.dirname(__file__))

postgres_local_base = os.environ.get('SQLALCHEMY_DATABASE_URI')
postgres_local_base_test = os.environ.get('SQLALCHEMY_DATABASE_URI_TEST')
postgres_production = os.environ.get('SQLALCHEMY_DATABASE_URI_PROD')

# database_name = 'feedand_api'

class BaseConfig:
    """Base configuration"""
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    BCRYPT_LOG_ROUNDS = 4
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = postgres_local_base


class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base_test

class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = postgres_production



app_configuration = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
