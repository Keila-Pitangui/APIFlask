import os 

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite://user.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False