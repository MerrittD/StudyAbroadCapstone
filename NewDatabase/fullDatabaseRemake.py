from databaseTesting import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Admin(db.Model):
    __tablename__ = "users"  # table name is users

    id = db.Column(db.INTEGER, primary_key=True)  # column in table for id for user, auto incremented
    username = db.Column(db.String(40),unique=True,nullable=False)  # column in table for the user's username that is entered at login, no repeats
    password = db.Column(db.String(40),unique=True,nullable=False)  # column in table for the user's password that is entered at login, no repeats


    # initializes instance of UserModel with the data for all columns given as parameters
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # saves the UserModel to the database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    # finds a row by specific username given as a parameter
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    # finds a row by specific id given as a parameter
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()






#Association Table refrences back to programs
programs_areas = db.Table('Programs_Areas',
db.Column('Program_id', db.Integer, db.ForeignKey('program.id'),primary_key=True),
db.Column('Area_id', db.Integer, db.ForeignKey('areas.id'),primary_key=True))


programs_terms = db.Table('Programs_Terms',
db.Column('program_id', db.Integer, db.ForeignKey('program.id'),primary_key=True),
db.Column('term_id', db.Integer, db.ForeignKey('terms.id'),primary_key=True))



programs_cities = db.Table('Programs_Cities',
db.Column('program_id', db.Integer, db.ForeignKey('program.id'),primary_key=True),
db.Column('city_id', db.Integer, db.ForeignKey('city.id'),primary_key=True))


cities_countries = db.Table('Cities_Countries',
db.Column('city_id', db.Integer, db.ForeignKey('city.id'),primary_key=True),
db.Column('country_id', db.Integer, db.ForeignKey('country.id'),primary_key=True))

programs_languages = db.Table('Programs_Languages',
db.Column('program_id', db.Integer, db.ForeignKey('program.id'),primary_key=True),
db.Column('language_id', db.Integer, db.ForeignKey('language.id'),primary_key=True))




class Program(db.Model):
	#Individual Attributes
	__tablename__ = "program"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	cost = db.Column(db.String(15))
	comm_eng = db.Column(db.Boolean) #yes or no
	research_opp =  db.Column(db.Boolean) #yes or no
	intership_opp = db.Column(db.Boolean)	#yes or no


	# This is to contain any specific data that does 
	# not fall into any of the above catorgies  
	description  = db.Column(db.String(5000))


	#Relationships
	programs_areas = db.relationship('Areas', secondary=programs_terms, lazy='subquery', 
								  backref=db.backref('area',lazy=True))

	programs_languages = db.relationship('Languages', secondary=programs_terms, lazy='subquery', 
								  backref=db.backref('language',lazy=True))

	cities = db.relationship("Cities", secondary=programs_cities, lazy='subquery', 
								  backref=db.backref('city',lazy=True))

	programs_terms = db.relationship('Term', secondary=programs_terms, lazy='subquery', 
								  backref=db.backref('term',lazy=True))
	


	#Individual Methods
	#optional method to set the porper string representation of the object
	def __repr__(self):
		return "<Program(Program ID='%d', Name='%s')>" % (self.id, self.name)

	def __init__(self, name, cost, com, res, intern, description,area,language,city,term):
		self.name = name
		self.cost = cost
		self.comm_eng = com
		self.research_opp = res
		self.intership_opp = intern
		self.description  = description
		

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()





class Area(db.Model):	
	#Individual Attributes
	__tablename__ = "areas"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	def __repr__(self):
		return "<Area(id='%d', name='%s')>" % (self.id, self.name)

	def __init__(self, name):
		self.name = name

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()




class Term(db.Model):	
	#Individual Attributes
	__tablename__ = "terms"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(10))
	#Individual Methods
	#optional method to set the porper string representation of the object
	def __repr__(self):
		return "<Term(id='%d', name='%s')>" % (self.id, self.name)

	def __init__(self, name):
		self.name = name

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()







class City(db.Model):
	#Individual Attributes
	__tablename__="city"
	id = db.Column(db.Integer, primary_key=True)
	city = db.Column(db.String(100))

	#Relationships
	countries = db.relationship('Countries', secondary=cities_countries, lazy='subquery', 
								  backref=db.backref('country',lazy=True))


	#Individual Methods
	#optional method to set the porper string representation of the object
	def __repr__(self):
		return "<City(City ID='%d', Name='%s')>" % (self.id, self.name)

	def __init__(self, id, name):
		self.id = id
		self.city = name

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()




#This is the class to define the country table with ids
class Country(db.Model):

	#Individual Attributes
	__tablename__ = "country"

	id = db.Column(db.Integer, primary_key=True)
	country = db.Column(db.String(100))

	#Individual Methods
	#optional method to set the porper string representation of the object
	def __repr__(self):
		return "<Country(Country ID='%d', Name='%s')>" % (self.id, self.name)

	def __init__(self, id, name):
		self.id = id
		self.country = name

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()
##Association Table refrences back to programs



class Language(db.Model):
	#Individual Attributes
	__tablename__ = "language"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))


	#Individual Methods
	#optional method to set the porper string representation of the object
	def __repr__(self):
		return "<Language(id='%d', name='%s')>" % (self.id, self.name)

	def __init__(self, name):
		self.area_name = name

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()
#  Websites Refrenced:
# https://docs.sqlalchemy.org/en/13/orm/tutorial.html
# https://github.com/Daniel-Wh/radiosonde/blob/master/models/station_model.py
# https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#many-to-many
# Use this for how to refrence a query: 
#  https://stackoverflow.com/questions/41270319/how-do-i-query-an-association-table-in-sqlalchemy


