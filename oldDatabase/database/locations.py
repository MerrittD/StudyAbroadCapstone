from db import db
#from sqlalchemy import ForeignKey, Table
#from sqlalchemy.orm import relationship
#from sqlalchemy.ext.declarative import declarative_base
#Base = declarative_base()



#Old way to construct the association tables 
	#Association table to programs.py
	#programs_cities = db.Table('Programs_Cities', Base.metadata,
	#	db.Column('program_id', db.Integer, db.ForeignKey('programs.id')),
	#	db.Column('city_id', db.Integer, db.ForeignKey('city.id')))


	#cities_countries = db.Table('Cities_Countries', Base.metadata,
	#	db.Column('city_id', db.Integer, db.ForeignKey('city.id')),
	#	db.Column('country_id', db.Integer, db.ForeignKey('country.id')))



class Programs_Cities(db.Model):
	#Individual Attributes
	__tablename__ = 'programs_cities'
	
	program_id = db.Column(db.Integer, db.ForeignKey('programs.id'))
	city_id = Column(db.Integer, db.ForeignKey('cities.id'))

	#Relationships
	program = db.relationship("Program",  back_populates="cities")
	city = db.relationship("City",  back_populates="programs")



class City(db.Model):
	#Individual Attributes
	__tablename__="cities"
	id = db.Column(db.Integer, primary_key=True)
	city = db.Column(db.String(100))

	#Relationships
	programs = db.relationship("Programs_Cities", back_populates="city")
	countries = db.relationship("Cities_Countries", back_populates="city")


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



class Cities_Countries(db.Model):
	#Individual Attributes
	__tablename__ = 'cities_countries'
	
	city_id = Column(db.Integer, db.ForeignKey('cities.id'))
	country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))

	#Relationships
	city = db.relationship("City",  back_populates="countries")
	country = db.relationship("Country",  back_populates="cities")



#This is the class to define the country table with ids
class Country(db.Model):

	#Individual Attributes
	__tablename__ = "countries"

	id = db.Column(db.Integer, primary_key=True)
	country = db.Column(db.String(100))


	#Relationship
	cities = db.relationship("Cities_Countries", back_populates="country")


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