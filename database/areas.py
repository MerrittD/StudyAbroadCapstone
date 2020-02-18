from db import db
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()



class Programs_Areas(db.Model):
	#Individual Attributes
	__tablename__ = 'programs_areas'
	
	program_id = db.Column(db.Integer, db.ForeignKey('programs.id'))
	area_id = Column(db.Integer, db.ForeignKey('areas.id'))
	
	#Relationships
	program = db.relationship("Program",  back_populates="programs")
	area = db.relationship("Area",  back_populates="areas")




class Area(db.Model):
	#Individual Attributes
	__tablename__ = "areas"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True, nullable=False)

#Relationship 
	programs = relationship("Programs_Areas", back_populates="program")

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
# method that finds the right row by the id given
	@classmethod
	def find_by_id(cls, _id):
		return cls.query.filter_by(id=_id).first()


# method that finds the right row by the name given
	@classmethod
	def find_by_name(cls, _name):
		return cls.query.filter_by(name=_name).first()