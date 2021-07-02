import os


class Config:
    SECRET_KEY = 'e3be6b00b6e7f53754498e54813ea190'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    #MAIL CONFIGURATION
    MAIL_SERVER = os.environ.get('MAIL_SERVER') #'smtp.gmail.com'#'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


