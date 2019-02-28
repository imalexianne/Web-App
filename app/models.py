from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'user',lazy="dynamic")
    comments = db.relationship('Comment',backref = 'user', lazy="dynamic")
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    description_path = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    category = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref = 'pitch',lazy="dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.filter_by(user_id=id).all()
        return pitches
    # users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'Pitch {self.description_path}'

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    description_all = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))

    # users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'Comment {self.description_all}'




# class User(UserMixin,db.Model):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer,primary_key = True)
#     username = db.Column(db.String(255),index = True)
#     email = db.Column(db.String(255),unique = True,index = True)
#     role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
#     password_hash = db.Column(db.String(255))