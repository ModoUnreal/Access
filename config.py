"""

(c) 2019 - ModoUnreal

config.py

"""


import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Creates default values for the config class.
       These values can be modified in child classes,
       for their respective purposes."""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'dev'
#    SQLALCHEMY_DATABASE_URI = "postgresql+pg8000://"


class ProductionConfig(Config):
    """Config class for production."""
    DEBUG = False


class StagingConfig(Config):
    """Config class for staging."""
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    """Config class for development."""
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    """Config class for testing."""
    TESTING = True
