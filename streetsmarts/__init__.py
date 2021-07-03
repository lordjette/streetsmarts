from flask import Flask
#from flask_jsglue import JSGlue
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager  #login_system, session
from flask_mail import Mail
from streetsmarts.config import Config
#virtualenv -p /usr/local/bin/python3.8 .virtualenvs/chapter07
from flask_migrate import Migrate #🏋️‍♂️🏋️‍♂️🏋️‍♂️

db = SQLAlchemy()
migrate = Migrate() #🏋️‍♂️🏋️‍♂️🏋️‍♂️
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view  = 'users.login'  #🔏🔏 raise a HTTP 401  to login define in route/blueprint routes, users.login= users is the name of blueprint
login_manager.login_message_category  = 'info'
mail = Mail()
# jsglue = JSGlue()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    # jsglue.init_app(app)
    migrate.init_app(app, db) #🏋️‍♂️🏋️‍♂️🏋️‍♂️
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)  #📮📮 FOR MAIL CONFIGURATION mail = Mail(app)

    from streetsmarts.users.routes import users
    from streetsmarts.posts.routes import posts
    from streetsmarts.main.routes import main
    from streetsmarts.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    
    return app


    '''
    # :flags:

    from flask import Flask
    from config import Config
    from flask_sqlalchemy import SQLAlchemy, event

    db = SQLAlchemy()

    def create_app():
        global db
        app = Flask(name)

    app.config....
    db.init_app(app)

    with app.app_context():
        @event.listens_for(db.engine, "first_connect")
        def connect(sqlite, connection_rec):
            sqlite.enable_load_extension(True)
            sqlite.execute("SELECT load_extension('C:\\spatialite32\\mod_spatialite')")
            sqlite.enable_load_extension(False)

        @event.listens_for(db.engine, "connect")
        def connect(sqlite, connection_rec):
            sqlite.enable_load_extension(True)
            sqlite.execute("SELECT load_extension('C:\\spatialite32\\mod_spatialite')")
            sqlite.enable_load_extension(False)

    return app

    app = create_app()

    from app import routes, models
    '''