# TODO create DB using flask migrate


'''
$ pip install flask-migrate

from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    migrate.init_app(app, db)
    return app
    
$ export FLASK_APP=run.py
$ flask db
$ flask db init
$ flask db migrate
$ flask db upgrade
'''

from streetsmarts import db
from streetsmarts.models import User, Post
user_1 = User(username = "Lordjette", email="lordjette.leigh@gmail.com", password= "password")
user_2 = User(username="Kaela", email="knfortuno@gmail.com", password="password")
user_3 = User(username = "Walker", email="xyzwalkeryoung38@gmail.com", password= "password")
user_4 = User(username="Ethen", email="xyzethenallen70@gmail.com", password="password")


db.session.add(user_1)
db.session.add(user_2)
db.session.add(user_3)
db.session.add(user_4)
db.session.commit()

User.query.all()
User.query.first()

User.query.filter_by(username='Kaela').all()
User.query.filter_by(username='Lordjette').first()

user = User.query.filter_by(username='Kaela').first()
user.id
user = User.query.get(1)
user

post_1 = Post(title='Blog 1', content='First Post Content!', user_id=user.id)
post_2 = Post(title='Blog 2', content='sECOND Post Content!', user_id=user.id)
db.session.add(post_1)
db.session.add(post_2)
db.session.add_all([post_1, post_2])
db.session.commit()
user.posts


# !hello
# ?hi
# *hello
# TODO: 
# @param myParam 
#! This is an alert


for post in user.posts:
    print(post.title)


Post.query.first()
post = Post.query.first()
post
post.user_id
post.author


db.drop_all()
db.create_all()


db.engine.table_names()  #  SHOW TABLES


