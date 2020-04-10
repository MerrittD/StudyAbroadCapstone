from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
url = 'sqlite:///newTestDatabase.db'
app.config['SQLALCHEMY_DATABASE_URI']=url
db = SQLAlchemy(app)	#creates an object for SQL to be used

# More info at https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application


