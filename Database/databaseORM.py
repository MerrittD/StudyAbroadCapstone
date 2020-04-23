from databaseConfiguration import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# used for deseralization for jsonify 
# code from https://stackoverflow.com/questions/7102754/jsonify-a-sqlalchemy-result-set-in-flask
def dump_datetime(val):
	if val is None:
		return None
	return [val.strftime("%Y-%m-%d"), val.strftime("%H:%M:%S")]

# Written by Luke Yates and Daniel Merritt
# Last Updated: 4/7/2020
# This is the ORM (Object Relationship Model) for the Study Abroad Program Finder
# 	Other Group Members: Ryan Wheeler, Mason Daniel, and Alyssa Case 


#This class handles all admin logins including username and passwords so that admins may edit the 
#	information on the site. A normal user will only be able to view the information. 
# This class was written by Daniel Whitney (refrence to GitHub repo at bottom of document)  
class Admin(db.Model):

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


#Association Tables refrences back to programs: 
# These tables hold all relationship rows between the 2 respected classes
areas = db.Table('Programs_Areas',
	db.Column('program_id', db.Integer, db.ForeignKey('Program.id')),
	db.Column('area_id', db.Integer, db.ForeignKey('Area.id')))

terms = db.Table('Programs_Terms',
	db.Column('program_id', db.Integer, db.ForeignKey('Program.id')),
	db.Column('term_id', db.Integer, db.ForeignKey('Term.id')))

languages = db.Table('Programs_Languages',
	db.Column('program_id', db.Integer, db.ForeignKey('Program.id')),
	db.Column('language_id', db.Integer, db.ForeignKey('Language.id')))

locations = db.Table('Programs_Locations',
	db.Column('program_id', db.Integer, db.ForeignKey('Program.id')),
	db.Column('location_id', db.Integer, db.ForeignKey('Location.id')))

programs = db.Table('Programs_Providers',
	db.Column('provider_id', db.Integer, db.ForeignKey('Provider.id')),
	db.Column('program_id', db.Integer, db.ForeignKey('Program.id')))



#This class defines the term table which holds all terms offered by a program
# It has a relationship back to the program class
class Provider(db.Model):	
	__tablename__='Provider'
	
	#Individual Attributes
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100),unique=True,nullable=False)


	program = db.relationship('Program',
						secondary=programs,  
						backref=db.backref('programs',lazy=True)
						)

	#Individual Methods
	def __repr__(self):
		return "<Provider(id='%d', name='%s')>" % (self.id, self.name)

	def __init__(self, name):
		self.name = name

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def add_program(self, newProgram): 
		self.program.append(newProgram)

	def remove_program(self, oldProgram): 
		self.program.remove(oldProgram)
		
	@classmethod
	def get_provider_id(cls, name):
		id = db.session.query(cls).filter(cls.name == name).first()
		if id is None: 
			return -1
		else:
			return id

	# finds a row by specific name given as a parameter
	@classmethod
	def find_by_name(cls, _name):
		return cls.query.filter_by(name=_name).first()

	@classmethod
	def return_all_providers(cls):
		return cls.query.order_by(cls.name).all()

	@property
	def serialize(self):
		return{
			'id':self.id,
			'name':self.name,
			'programs':self.programSerial
			}

	@property
	def programSerial(self):
		return [i.serialize for i in self.program]
		
#This class defines the area class. It is to hold all areas of study that can exist 
#	throught a study abroad program
#	It has a relationship back to the program class
class Area(db.Model):	
	__tablename__='Area'

	#Individual Attributes
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100),unique=True,nullable=False)

	#Individual Methods
	def __repr__(self):
		return "<Area(id='%d', name='%s')>" % (self.id, self.name)

	def __init__(self, name):
		self.name = name

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def get_area_id(cls,name):
		id = db.session.query(cls).filter(cls.name == name).first()
		if id is None: 
			return -1
		else:
			return id

	# finds a row by specific username given as a parameter
	@classmethod
	def find_by_name(cls, _name):
		return cls.query.filter_by(name=_name).first()

	@property
	def serialize(self):
		return{
			'id':self.id,
			'name':self.name
			}


#This class defines the term table which holds all terms offered by a program
# It has a relationship back to the program class
class Term(db.Model):	
	__tablename__='Term'
	
	#Individual Attributes
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(10),unique=True,nullable=False)

	#Individual Methods
	def __repr__(self):
		return "<Term(id='%d', name='%s')>" % (self.id, self.name)

	def __init__(self, name):
		self.name = name

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()
		
	@classmethod
	def get_term_id(cls,name):
		id = db.session.query(cls).filter(cls.name == name).first()
		if id is None: 
			return -1
		else:
			return id

	# finds a row by specific username given as a parameter
	@classmethod
	def find_by_name(cls, _name):
		return cls.query.filter_by(name=_name).first()

	@property
	def serialize(self):
		return{
			'id':self.id,
			'name':self.name
			}


#This class defines the city table which holds all cities a program can be offered in
# It has a relationship back to the program class
class Location(db.Model):
	__tablename__='Location'
	
	#Individual Attributes
	id = db.Column(db.Integer, primary_key=True)
	city = db.Column(db.String(100),nullable=True)
	country= db.Column(db.String(100),nullable=False)
	

	#Individual Methods
	def __repr__(self):
		return "<Location(id='%d', city name='%s', country name='%s')>" % (self.id, self.city, self.country)

	def __init__(self, nameCity,nameCountry):
		self.city = nameCity
		self.country= nameCountry

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def get_location_id(cls, nameCity, nameCountry):
		id = db.session.query(cls).filter(cls.city == nameCity).filter(cls.country == nameCountry).first()
		if id is None: 
			return -1
		else:
			return id

	# finds a row by specific id given as a parameter
	@classmethod
	def find_by_id(cls, _id):
		return cls.query.filter_by(id=_id).first()

	# finds a row by specific username given as a parameter
	@classmethod
	def find_by_name(cls, _city, _country):
		return cls.query.filter_by(city=_city).filter_by(country=_country).first()
	
	@property
	def serialize(self):
		return{
			'id':self.id,
			'city':self.city,
			'country':self.country
			}


# This class defines the Langue class which holds all foreign languages a proram can offer to teach
#	It has a relationship back to the program class
class Language(db.Model):
	__tablename__='Language'

	#Individual Attributes
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50),unique=True,nullable=False)

	#Individual Methods
	def __repr__(self):
		return "<Language(id='%d', name='%s')>" % (self.id, self.name)

	def __init__(self, name):
		self.name = name

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def get_language_id(cls,name):
		id = db.session.query(cls).filter(cls.name == name).first()
		if id is None: 
			return -1
		else:
			return id

	# finds a row by specific username given as a parameter
	@classmethod
	def find_by_name(cls, _name):
		return cls.query.filter_by(name=_name).first()

	@property
	def serialize(self):
		return{
			'id':self.id,
			'name':self.name
			}


#This class defines the table for all programs stored. The table holds specific attributes listed under 
#	Individual Attributes. The relationships define connections to the 4 of the 5 association tables listed above.
#	The relationships to the "children" classes are only defined here, but backrefrence upon update. 
class Program(db.Model):
	__tablename__='Program'

	#Individual Attributes
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100),unique=True,nullable=False)

	comm_eng = db.Column(db.Boolean,nullable=False)		#yes or no
	research_opp =  db.Column(db.Boolean,nullable=False)	#yes or no
	intership_opp = db.Column(db.Boolean,nullable=False)	#yes or no

	date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                       onupdate=db.func.current_timestamp())
	
	cost = db.Column(db.String(15), nullable=True)
	cost_stipulations = db.Column(db.String(500), nullable=True)

	description  = db.Column(db.String(5000), nullable=True)
	url = db.Column(db.String(5000), nullable=True)

	#Relationships
	area = db.relationship('Area',
							secondary=areas, 
							backref=db.backref('areas',lazy=True)
							)

	language = db.relationship('Language',
								secondary=languages,
								backref=db.backref('languages',lazy=True)
								)

	location = db.relationship('Location',
						secondary=locations, 
						backref=db.backref('locations',lazy=True)
						)

	term = db.relationship('Term',
						secondary=terms,  
						backref=db.backref('terms',lazy=True)
						)
	

	#Individual Methods
	#optional method to set the porper string representation of the object
	def __repr__(self):
		return "<Program(Program ID='%d', Name='%s')>" % (self.id, self.name)

	def __init__(self, name, com, res, intern, cost, cost_stipulations, description, url):
		#This initilizes the program specific fields
		self.name = name
		self.comm_eng = com
		self.research_opp = res
		self.intership_opp = intern
		self.cost = cost
		self.cost_stipulations = cost_stipulations
		self.description  = description
		self.url  = url


	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	#These methods will be by the API to add and remove any property that falls 
	# under the many to many relationship. 
	def add_language(self, newLanguage): 
		self.language.append(newLanguage)

	def remove_language(self, oldLanguage): 
		self.language.remove(oldLanguage)

	def add_area(self, newArea): 
		self.area.append(newArea)

	def remove_area(self, oldArea): 
		self.area.remove(oldArea)

	def add_term(self, newTerm): 
		self.term.append(newTerm)

	def remove_term(self, oldTerm): 
		self.term.remove(oldTerm)

	def add_location(self, newLocation):
		self.location.append(newLocation)

	def remove_location(self, oldLocation): 
		self.location.remove(oldLocation)


	#These methods will be used for sorting when the user initilizes 
	@classmethod
	def return_all_programs(cls):
		return cls.query.order_by(cls.name).all()

	@classmethod
	def sort_by_language(cls, desiredLanguage):
		return cls.query.join(Programs_Languages).join(Language).filter(Programs_Languages.c.language_id == get_language_id(desiredLanguage)).all()

	@classmethod
	def sort_by_term(cls, desiredTerm):
		return cls.query.join(Programs_Terms).join(Term).filter(Programs_Terms.c.term_id == get_term_id(desiredTerm)).all()

	@classmethod
	def sort_by_area(cls, desiredArea):
		return cls.query.join(Programs_Areas).join(Area).filter(Programs_Areas.c.area_id == get_area_id(desiredArea)).all()

	@classmethod
	def sort_by_location(cls, desiredCountry):
		return cls.query.join(Programs_Locations).join(Location).filter(Programs_Locations.c.location_id == get_location_id(desiredCountry)).all()

	@classmethod
	def get_program_id(cls, name):
		id = db.session.query(cls).filter(cls.name == name).first()
		if id is None: 
			return -1
		else:
			return id

	# finds a row by specific id given as a parameter
	@classmethod
	def find_by_id(cls, _id):
		return cls.query.filter_by(id=_id).first()

	# finds a row by specific username given as a parameter
	@classmethod
	def find_by_name(cls, _name):
		return cls.query.filter_by(name=_name).first()

	@property
	def serialize(self):
		#id = db.Column(db.Integer, primary_key=True)
		#name = db.Column(db.String(100),unique=True,nullable=False)

		#comm_eng = db.Column(db.Boolean,nullable=False)		#yes or no
		#research_opp =  db.Column(db.Boolean,nullable=False)	#yes or no
		#intership_opp = db.Column(db.Boolean,nullable=False)	#yes or no

		#date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
		#date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                       #onupdate=db.func.current_timestamp())
	
		#cost = db.Column(db.String(15), nullable=True)
		#cost_stipulations = db.Column(db.String(500), nullable=True)

		#description  = db.Column(db.String(5000), nullable=True)
		#url = db.Column(db.String(5000), nullable=True)
		return{ 
			'id': self.id,
			'name':self.name,
			'comm':self.comm_eng,
			'research':self.research_opp,
			'intern':self.intership_opp,
			'create':dump_datetime(self.date_created),
			'mod':dump_datetime(self.date_modified),
			'cost':self.cost,
			'stip':self.cost_stipulations,
			'desc':self.description,
			'url':self.url,
			'area':self.seralize_manyToManyArea,
			'lang':self.seralize_manyToManyLang,
			'loc':self.seralize_manyToManyLoc,
			'term':self.seralize_manyToManyTerm
			}
	@property
	def seralize_manyToManyArea(self):
		return [i.serialize for i in self.area]
	@property
	def seralize_manyToManyLang(self):
		return [i.serialize for i in self.language]
	@property
	def seralize_manyToManyLoc(self):
		return [i.serialize for i in self.location]
	@property
	def seralize_manyToManyTerm(self):
		return [i.serialize for i in self.term]



		

#  Websites Refrenced:
# https://docs.sqlalchemy.org/en/13/orm/tutorial.html
# https://github.com/Daniel-Wh/radiosonde/blob/master/models/station_model.py
# https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#many-to-many
# Use this for how to refrence a query: 
#  https://stackoverflow.com/questions/41270319/how-do-i-query-an-association-table-in-sqlalchemy
# https://stackoverflow.com/questions/32938475/flask-sqlalchemy-check-if-row-exists-in-table
# https://stackoverflow.com/questions/12154129/how-can-i-automatically-populate-sqlalchemy-database-fields-flask-sqlalchemy


