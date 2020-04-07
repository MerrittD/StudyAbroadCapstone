from fullDatabaseRemake import Admin,areas,terms,locations,languages,programs,Program,Area,Term,Location,Language,Provider 
from databaseTesting import db
import os

db.create_all()
db.session.commit()

#This file is to be run upon initial setup of the database, and should pull from a 
#backup file inorder to populate new database 



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
#  provider.save_to_database()

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
def create_new_program(providerName, programName, cost, com, res, intern, description, url, areas, terms, languages, locations): 
    #-----------------------------PROVIDER RELATIONSHIP----------------------------
    # Check if the provider already exist, if it doesn't then make a new provider
    if(Provider.get_provider_id(providerName) == -1):
        prov = Provider(providerName)
        prov.save_to_db()
    else: 
        prov = Provider.find_by_name(providerName)

    # Check if the program already exist, if it doesn't then make a new program
    if(Program.get_program_id(programName) == -1):
        prog = Program(programName, cost, com, res, intern, description, url)
        prog.save_to_db()
    else: 
        prog = Program.find_by_name(programName)

    #Add the program to the provider
    prov.add_program(prog)
    prov.save_to_db()


    #-----------------------------PROGRAM RELATIONSHIPS----------------------------
    # AREA, TERM, LANGUAGES, LOCATION

    # AREA: 
    # Cyle through all area names: check to see if the area already exist in the db, 
    #    if it doesn't, add it to the program and create the relationship. 
    for i in areas:
        if(Area.get_area_id(i) == -1):
            tempArea = Area(i)
            tempArea.save_to_db()
        else: 
            tempArea = Area.find_by_name(i)
        
        prog.add_area(tempArea)
        prog.save_to_db()
        #might need save to db methods

    # TERM: 
    # Cyle through all term names: check to see if the term already exist in the db, 
    #    if it doesn't, add it to the program and create the relationship. 
    for i in terms:
        if(Term.get_term_id(i) == -1):
            tempTerm = Term(i)
            tempTerm.save_to_db()
        else: 
            tempTerm = Term.find_by_name(i)
        
        prog.add_term(tempTerm)
        prog.save_to_db()
        #might need save to db methods

    # LANGUAGES: 
    # Cyle through all term names: check to see if the term already exist in the db, 
    #    if it doesn't, add it to the program and create the relationship. 
    for i in languages:
        if(Language.get_language_id(i) == -1):
            tempLanguage = Language(i)
            tempLanguage.save_to_db()
        else: 
            tempLanguage = Language.find_by_name(i)
        
        prog.add_language(tempLanguage)
        prog.save_to_db()
        #might need save to db methods

    # LOCATION: 
    # Cyle through all term names: check to see if the term already exist in the db, 
    #    if it doesn't, add it to the program and create the relationship. 
    for i in locations:
        if(Location.get_location_id(i[0], i[1]) == -1):
            tempLocation = Location(i[0], i[1])
            tempLocation.save_to_db()
        else: 
            tempLocation = Location.find_by_name(i[0], i[1])
        
        prog.add_location(tempLocation)
        prog.save_to_db()
        #might need save to db methods


def Convert(string): 
    li = list(string.split("; ")) 
    return li 

def ConvertLocation(string):
    l = Convert(string)
    returnList = []
    for i in l:
        returnList.append(list(i.split(", "))) 
    return returnList


def main():
   #-----------------------------TEMPORARY VARIABLES FOR TESTING----------------------------
#    providerName = "A1"
#    programName = "SU Amsterdam" 
#    com = True 
#    res = False
#    intern = True
#    cost = "$6,215"
#    cost_stipulations = "Schooling Only"
#    description = "This is the amsterdam description"
#    url = "https://www.southwestern.edu/study-abroad/study-abroad-programs/su-amsterdam/index.php"

    #all relationships will be lists to accomdiate multiple entries
#    areas = ["Computer Science", "Communication"]
#    terms = ["Summer 1"]
#    languages = ["Dutch"]
#    locations = [["Amsterdam", "Netherlands"]]    #This will be a list of list like [city name, country name] representing a location


    # Format for File Reading 
    # 1. Provider Name
    # 2. Program Name
    # 3. Community Engagement 
    # 4. Research Oppurtinities
    # 5. Internship Oppurtunities
    # 6. Cost
    # 7. Cost Stipulations
    # 8. Description
    # 9. Url
    # 10. Areas
    # 11. Terms
    # 12. Languages
    # 13. Locations

    #References for work: 
    #https://tecadmin.net/count-number-of-lines-in-file-python/
    #https://www.geeksforgeeks.org/python-program-convert-string-list/
    # https://stackoverflow.com/questions/4060221/how-to-reliably-open-a-file-in-the-same-directory-as-a-python-script

    #This is tested in testFileReading.py in previous database test

    fname = "C:\Users\lukey\Documents\GitHub\StudyAbroadCapstone\NewDatabase\DataImportFile.txt"
    lineCount = 1
    with open(fname, 'r') as f:
        for eachLine in f:
            line = eachLine.strip()
            if(lineCount % 14 == 1):
                #Provider
                providerName = line

            if(lineCount % 14 == 2):
                #Program
                programName = line

            if(lineCount % 14 == 3):
                #Community Engagement
                com = line

            if(lineCount % 14 == 4):
                #Research Oppurtinities
                res = line

            if(lineCount % 14 == 5):
                #Internship Oppurtunities
                intern = line

            if(lineCount % 14 == 6):
                #Cost
                cost = line 

            if(lineCount % 14 == 7):
                #Cost Stipulations
                cost_stipulations = line

            if(lineCount % 14 == 8):
                #Description
                description = line

            if(lineCount % 14 == 9):
                #Url
                url = line

            if(lineCount % 14 == 10):
                #Areas
                areas = Convert(line)

            if(lineCount % 14 == 11):
                #Terms
                terms = Convert(line)

            if(lineCount % 14 == 12):
                #Languages
                languages = Convert(line)

            if(lineCount % 14 == 13):
                #Locations
                locations = ConvertLocation(line)

            if(lineCount % 14 == 0): 
                create_new_program(providerName, programName, cost, com, res,
                                  intern, description, url, areas, terms, languages, locations)
            lineCount += 1
            


if __name__ == '__main__':
    main()


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