#from __init__ import db
from flask import Flask
import flask_sqlalchemy
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


#db.app = app


class Project(db.Model):
    __tablename__ = 'project'
    project_id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100))
    project_desc = db.Column(db.Text, nullable=True)
    project_status = db.Column(db.String(100))
    project_stack = db.Column(db.String(100), nullable=True)
    max_members = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    client_name = db.Column(db.String(100), nullable=True)
    client_email = db.Column(db.String(100), nullable=True)
    client_phone = db.Column(db.Integer, nullable=True)

    # constructor of Project
    def __init__(self, project_name, project_desc,  project_status, project_stack=None,
                max_members=None, client_phone=None,  client_name=None, client_email=None, date=None):
        """

        :type date: object
        """
        self.project_name = project_name
        self.client_name = client_name
        self.max_members = max_members
        self.project_desc = project_desc
        self.project_status = project_status
        self.project_stack = project_stack
        self.client_phone = client_phone
        self.client_email = client_email
        self.date = date

    def __repr__(self):
        return '<Project %r>' % self.project_name

    def serialize(self):
        # todo в serialize указать все поля, даже если они пустые
        return {'project_id': self.project_id, 'project_desc': self.project_desc, 'client_name': self.client_name,
                'client_phone': self.client_phone, 'project_status': self.project_status,
                'project_stack': self.project_stack, 'date': self.date,
                'client_email': self.client_email, 'max_members': self.max_members, 'project_name': self.project_name}


#class ProjectSchema(ma.Schema):
#    class Meta:
#        model = Project
        #load_instance = True
        #sql_session = db.session


# class for the signing up to the project
class Signup(db.Model):
    signup_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, ForeignKey(
        "project.project_id"), nullable=False)
    signup_name = db.Column(db.String(100), nullable=True)
    sign_up_github = db.Column(db.String(100), nullable=True)
    signup_email = db.Column(db.String(100))

    # todo project_id must be array -> projects_ids

    # constructor of Signup
    def __init__(self, signup_id, signup_email, project_id, signup_name=None, sign_up_github=None):
        self.project_id = project_id
        self.signup_id = signup_id
        self.signup_email = signup_email
        self.signup_name = signup_name
        self.sign_up_github = sign_up_github

    def __repr__(self):
        return '<Signup %r>' % self.signup_name

    def serialize(self):
        return {'signup_email': self.signup_email, 'signup_name': self.signup_name,
                'sign_up_github': self.sign_up_github}


# class for voting for the project with the member like
class Vote(db.Model):
    project_id = db.Column(db.Integer, ForeignKey(
        "project.project_id"), nullable=False)
    voter_name = db.Column(db.String(100), nullable=True)
    voter_slack_name = db.Column(db.String(100), nullable=True)
    voter_email = db.Column(db.String(100), primary_key=True)

    def __init__(self, project_id, voter_email, voter_name=None, voter_slack_name=None):
        self.voter_name = voter_name
        self.voter_slack_name = voter_slack_name
        self.voter_email = voter_email

    def __repr__(self):
        return '<Vote %r>' % self.voter_name

    def serialize(self):
        return {'voter_name': self.voter_name, 'voter_slack_name': self.voter_slack_name,
                'voter_email': self.voter_email}


# class for admin page
class Admin(db.Model):
    admin_name = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100))
    chapter_name = db.Column(db.String(100))

    def __init__(self, admin_name, password, chapter_name):
        self.admin_name = admin_name
        self.password = password
        self.chapter_name = chapter_name

    def __repr__(self):
        return '<Admin %r>' % self.admin_name


def init_db():
    db.create_all()

if __name__ == '__main__':
    init_db()
