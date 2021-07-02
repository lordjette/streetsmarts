#import secrets; secrets.token_hex(16);
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from streetsmarts import db, login_manager
from flask_login import UserMixin #default implementations for all of these properties and methods. is_authenticated criteria of login_required, is_active, is_anonymous, get_id() in  user_loader , 

from sqlalchemy.dialects.postgresql import JSON, JSONB
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import Index




@login_manager.user_loader  # :fire::fire::fire: callback, function with decorator, reloading the user from the user_id stored in the session, actual connection between flask login and the database
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin): # UserMixin :arrow_right::arrow_right:  it adds attributes of user class
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20),  nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref = 'author', lazy=True)  ##one to many relationship, db.relationship('[child model name eg Post same as below]'), 
            #author = is like fake column, virtual column
            # for many to many use append

            #💑 Flask-SQLAlchemy ORM Relationship lazy: select/true, joined/false, subquery, dynamic
            #💑 SQLAlchemy ORM as Base Types of Relationship loading techniques 
                # {:one: [lazy='select'], :two:[lazy=joined], :three:[lazy=subquery], :four:[lazy=selectin], 
                #   :five:[lazy:raise], :six:[lazy='noload']}
            
    #method for token  reset 
    def get_reset_token(self, expires_sec= 60):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')  #user_id is just a variable get param/method, you can change it

    #methods that verified tokens
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):  #🧙🧙 underscore method || magic methods || special method, this how the object printed out, requirements in model
        #return f"User('{self.username}', '{self.email}', '{self.image_file}')"
        return '<User {}>'.format(self.username)
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default = datetime.utcnow) #case sensitive DateTime
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  #kaya siya lower case user because this is default set of DB (user = User)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"



class RecordsMetadata(db.Model): #with 👺🔰 JSON
    created = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=False)
    id = db.Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False)
    version_id = db.Column(db.Integer, nullable=False)
    json = db.Column(JSONB)

    Index('idx_record_metadatax', version_id, postgresql_ops={'version_id':''}, postgresql_using='btree')

    def __repr__(self):
        return f"RecordsMetadata('{self.created}', '{self.updated}', '{self.id}', '{self.json}')"

class PidstoreRecid(db.Model): 
    recid = db.Column(db.Integer, primary_key=True)

class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(JSON)
    pid_value = db.Column(db.String(255))
    pid_type = db.Column(db.String(3))
    age = db.Column(db.Integer)

    Index('idx_age', pid_value, pid_type, postgresql_ops={'pid_value':'varchar_pattern_ops', 'pid_type':''}, postgresql_using='btree')
    #BTREE: int4_ops, text_pattern_ops, varchar_pattern_ops, bpchar_pattern_ops, and name_pattern_ops
    def __repr__(self):
        return f"Person('{self.data}', '{self.pid_value}', '{self.pid_type}', '{self.age}')"