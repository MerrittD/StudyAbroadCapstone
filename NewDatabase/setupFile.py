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

#  program.add_language(languageName)
#  program.add_area(areaName)
#  program.add_term(termName)
#  program.add_location(locationCity, locationCountry)

#  program.remove_language(languageName)
#  program.remove_area(areaName)
#  program.remove_term(termName)
#  program.remove_location(locationCity, locationCountry)


# This script below is to test all methods for the database
#    I have used the data on the "Dummy Study Abroad Programs Data" on the Project Drive

#This is a generic script to populate an entire program
# These are data sheets that can be filled in with different information
def create_new_program(): 
    # all variables for a new program to be added
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
    areas = []
    languages = [[]]    #This will be a list of list like [city name, country name] representing a location


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




    

    lang = Language(self, langName)
    loc = Location(self, city, country)
    term = Term(self, termName)
    area = Area(self, areaName)



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