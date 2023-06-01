import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    def __init__(self):
        self.DEBUG = False
        self.TESTING = False
        self.CSRF_ENABLED = True
        self.SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']