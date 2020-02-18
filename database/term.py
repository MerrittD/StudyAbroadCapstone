from db import db
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Association Table refrences back to programs
# programs_terms = db.Table('Programs_Terms', Base.metadata,
#	db.Column('program_id', db.Integer, db.ForeignKey('programs.id')),
#	db.Column('term_id', db.Integer, db.ForeignKey('term.id')))


class Programs_Terms(db.Model):
	#Individual Attributes
	__tablename__ = 'programs_terms'
	
	program_id = db.Column(db.Integer, db.ForeignKey('programs.id'))
	term_id = Column(db.Integer, db.ForeignKey('terms.id'))
	
	#Relationships
	program = db.relationship("Program",  back_populates="terms")
	term = db.relationship("Term",  back_populates="programs") 
	



class Term(db.Model):	
	#Individual Attributes
	__tablename__ = "terms"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(10))


	#Relationship
	programs = db.relationship("Programs_Terms", back_populates="term")


	#Individual Methods
	#optional method to set the porper string representation of the object
	def __repr__(self):
		return "<Term(id='%d', name='%s')>" % (self.id, self.name)

	def __init__(self, name):
		self.term_name = name

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()
