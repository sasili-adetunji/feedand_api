import os

basedir = os.path.abspath(os.path.dirname(__file__))

postgres_local_base = 'postgresql://postgres:AjibolA2016?@localhost/'
database_name = 'feedand_api'

class BaseConfig:
    """Base configuration"""
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    BCRYPT_LOG_ROUNDS = 4
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name


class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + '_test'

class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql:///example'



app_configuration = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
