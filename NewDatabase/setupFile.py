from fullDatabaseRemake import Admin,areas,terms,locations,languages,Program,Area,Term, Location, Language 
from databaseTesting import db



#This file is to be run upon initial setup of the database, and should pull from a 
#backup file inorder to populate new database 

db.create_all()

# Constructors: 
#   - Provider(self, name):
#   - Program(self, name, cost, com, res, intern, description, url):
#   - Language(self, name):
#   - Location(self, city, country):
#   - Term(self, name):
#   - Area(self, name):
#   - Admin(self, username, password): 

# How to add a program to a provider: 
#   Use constructor to create a new provider
#   use the add_object or remove_object methods and add and remove
#   
#   You can add or remove: 
#       - A Program from a Provider
#
#       - A Language from a Program
#       - A Term from a Program
#       - A Location from a Program
#       - An Area from a Program

# How to add and remove relationships between objects (example- connect a language to a program): 
#  provider.add_program(programName)
#  provider.remove_program(programName)

#  program.add_language(language)
#  program.add_area(area)
#  program.add_term(term)
#  program.add_location(location)

#  program.remove_language(language)
#  program.remove_area(area)
#  program.remove_term(term)
#  program.remove_location(location)


# This script below is to test all methods for the database
#    I have used the data on the "Dummy Study Abroad Programs Data" on the Project Drive

#This is a generic script to populate an entire program
# These are data sheets that can be filled in with different information
def create_new_program(): 
    #-----------------------------TEMPORARY VARIABLES----------------------------
    providerName = NULL
    programName = NULL
    cost = NULL 
    com = NULL 
    res = NULL 
    intern = NULL
    description = NULL
    url = NULL

    #all relationships will be lists to accomdiate multiple entries
    areas = []
    terms = []
    languages = []
    locations = [[]]    #This will be a list of list like [city name, country name] representing a location


     #-----------------------------PROVIDER RELATIONSHIP----------------------------
     # Check if the provider already exist, if it doesn't then make a new provider
    if(get_provider_id(providerName) == -1):
        prov = Provider(providerName)
    else: 
        prov = find_by_name(providerName)

    # Check if the program already exist, if it doesn't then make a new program
    if(get_program_id(name) == -1):
        prog = Program(programName, cost, com, res, intern, description, url)
    else: 
        prog = find_by_name(programName)

    #Add the program to the provider
    prov.add_program(programName)

    #might need save to db methods for the provider and program before performing other operations


    #-----------------------------PROGRAM RELATIONSHIPS----------------------------
    # AREA, TERM, LANGUAGES, LOCATION

    # AREA: 
    # Cyle through all area names: check to see if the area already exist in the db, 
    #    if it doesn't, add it to the program and create the relationship. 
    for i in areas:
        if(get_area_id(i) == -1):
            tempArea = Area(i)
        else: 
            tempArea = find_by_name(i)
        
        prog.add_area(tempArea)
        #might need save to db methods

    # TERM: 
    # Cyle through all term names: check to see if the term already exist in the db, 
    #    if it doesn't, add it to the program and create the relationship. 
    for i in terms:
        if(get_term_id(i) == -1):
            tempTerm = Term(i)
        else: 
            tempTerm = find_by_name(i)
        
        prog.add_term(tempTerm)
        #might need save to db methods

    # LANGUAGES: 
    # Cyle through all term names: check to see if the term already exist in the db, 
    #    if it doesn't, add it to the program and create the relationship. 
    for i in languages:
        if(get_language_id(i) == -1):
            tempLanguage = Language(i)
        else: 
            tempLanguage = find_by_name(i)
        
        prog.add_language(tempLanguage)
        #might need save to db methods

    # LOCATION: 
    # Cyle through all term names: check to see if the term already exist in the db, 
    #    if it doesn't, add it to the program and create the relationship. 
    for i in locations:
        if(get_location_id(i[1], i[2]) == -1):
            tempLocation = Location(i[1], i[2])
        else: 
            tempLocation = find_by_name(i[1], i[2])
        
        prog.add_location(tempLocation)
        #might need save to db methods






#Here will be a loop to add data to the database from files 
# For every program in the file for database population
    # create the program
    #newprogram = Program('all things needed')
    #db.session.add(newprogram)
#once we are done adding programs,      
#db.session.commit()
#admins can be loaded in with a different loop before the commit
#if we use a text document to populate, we can take the strings in and use .split()
 #however, this isnt secure and there has to be a better way 
#newAdmin= Admin("test","1234")
#newProgram = Program("TestingProgram","30",True,True,True, "This is for testing","CS","Spanish","Madrid","Spain","Spring")
#Newprogram = Program("Spain shit", "500",True,True,True,"This is for testing, we wish a study abroad only cost 500","Spanish","Buisness","Spring","Madrid","Spain")
#Newprogram.save_to_db()