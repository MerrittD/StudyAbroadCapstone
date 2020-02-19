from db import db
#from sqlalchemy import ForeignKey
#from sqlalchemy.orm import relationship
from areas import Programs_Areas
from languages import Programs_Languages
from locations import Programs_Cities
from term import Programs_Terms

#  Websites Refrenced:
# https://docs.sqlalchemy.org/en/13/orm/tutorial.html
# https://github.com/Daniel-Wh/radiosonde/blob/master/models/station_model.py
# https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#many-to-many
# Use this for how to refrence a query: 
#  https://stackoverflow.com/questions/41270319/how-do-i-query-an-association-table-in-sqlalchemy


class Program(db.Model):
	#Individual Attributes
	__tablename__ = "programs"

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
	areas = db.relationship("Programs_Areas", back_populates="program")
	languages = db.relationship("Programs_Languages", back_populates="program")
	cities = db.relationship("Programs_Cities", back_populates="program")
	terms = db.relationship("Programs_Terms", back_populates="program")
	


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
