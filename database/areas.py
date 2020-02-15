from db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()



#Association Table refrences back to programs
programs_areas = Table('Programs_Areas', Base.metadata,
db.Column('program_id', db.Integer, ForeignKey('programs.id')),
db.Column('area_id', db.Integer, ForeignKey('areas_of_study.id')))



class Area(db.Model):

#Individual Attributes
	__tablename__ = "areas_of_study"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True, nullable=False)


#Relationship 
	programs = relationship("Program", secondary=programs_areas, back_populates="areas")


#Individual Methods
	#optional method to set the porper string representation of the object
def __repr__(self):
	return "<Area(id='%d', name='%s')>" % (self.id, self.name)

def __init__(self, name):
	self.name = name

def save_to_db(self):
	db.session.add(self)
	db.session.commit()


#Class Methods
	#This is where search methods will go. There is a reference of how to 
	# in the programs file
	
# method that finds the right row by the id given
	@classmethod
	def find_by_id(cls, _id):
		return cls.query.filter_by(id=_id).first()


# method that finds the right row by the name given
	@classmethod
	def find_by_name(cls, _name):
		return cls.query.filter_by(name=_name).first()
		
# 
	#@classmethod
	#def find_programs(cls, _):