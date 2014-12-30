import os

# default config
class BaseConfig(object):
    ''' Base configuration '''
    DEBUG = False
    SSL = True
    STRIPE_SECRET_KEY = 'YOUR_LIVE_SECRET_KEY'

class TestConfig(BaseConfig):
    ''' Test configuration '''
    DEBUG = True
    TESTING = True
    SSL = False
    STRIPE_SECRET_KEY = 'YOUR_TEST_SECRET_KEY'

class DevelopmentConfig(BaseConfig):
    ''' Development configuration '''
    DEBUG = True
    SSL = False
    STRIPE_SECRET_KEY = 'YOUR_TEST_SECRET_KEY'

class ProductionConfig(BaseConfig):
    ''' Production configuration '''
    DEBUG = False
