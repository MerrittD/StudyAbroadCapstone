from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app= Flask(__name__)
url = 'sqlite:///testDatabase.db'
app.config['SQLALCHEMY_DATABASE_URI']=url
db = SQLAlchemy(app)	#creats an object for SQL to be used


# More info at https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application


# this was for testing and can be ignored/ used as a template for other files 
#class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(80), unique=True, nullable=False)
#    email = db.Column(db.String(120), unique=True, nullable=False)

#    def __repr__(self):
#        return '<User %r>' % self.username
