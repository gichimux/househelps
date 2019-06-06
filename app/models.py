from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime 


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    fname = db.Column(db.String(255),index = True) 
    lname = db.Column(db.String(255),index = True) 
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    category = db.relationship('Category',backref = 'users',lazy="dynamic")
    review = db.relationship('Review',backref = 'users',lazy="dynamic")
    jobs = db.relationship('Job',backref = 'users',lazy="dynamic")
    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls,id):
        reviews = Review.query.filter_by(user_id=id).all()
        return comments

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
            return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic") 

    def __repr__(self):
        return f'User {self.name}'

class Category(db.Model):
    '''
    Function that defines different categories of pitches
    '''
    __tablename__ ='user_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

class Review(db.Model):
    
    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    review = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_review(self):
        '''
        Function that saves reviews
        '''
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_reviews(cls,id):
        reviews = Review.query.filter_by(user_id=id).all()

        return reviews

class Job(db.Model):
    '''
    job class to define Pitch Objects
    '''
    __tablename__ = 'job'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
        

    def save_job(self):
        '''
        Function that saves jobs
        '''
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_all_jobs(cls):
        '''
        Function that queries the databse and returns all the jobs
        '''
        return Job.query.all()

    


