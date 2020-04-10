from fullDatabaseRemake import Admin,areas,terms,locations,languages,programs,Program,Area,Term,Location,Language,Provider 
import os


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
def create_new_program(providerName, programName, com, res, intern, cost, cost_stipulations, description, url, areas, terms, languages, locations): 
    #-----------------------------PROVIDER RELATIONSHIP----------------------------
    # Check if the provider already exist, if it doesn't then make a new provider
    if(Provider.get_provider_id(providerName) == -1):
        prov = Provider(providerName)
        prov.save_to_db()
    else: 
        prov = Provider.find_by_name(providerName)

    # Check if the program already exist, if it doesn't then make a new program
    if(Program.get_program_id(programName) == -1):
        prog = Program(programName, com, res, intern, cost, cost_stipulations, description, url)
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
    db.create_all()
    db.session.commit()

    #-----------------------------TEST PROGRAM # 1-------------------------------
    providerName = "A1"
    programName = "SU Amsterdam" 
    com = True 
    res = False
    intern = True
    cost = "$6,215"
    cost_stipulations = "Schooling Only"
    description = "This course is designed to increase awareness and knowledge of cross cultural differences in sexual attitudes and behaviors. Specifically, students will learn how sex education, sex work, and sexual health differ in the Netherlands compared to the United States.  In addition to this in-depth comparative analysis of sexuality, students will study the history of marginalized groups in the Netherlands, including the LGBT community. Students will also be immersed in Dutch culture through guided tours, visits to museums, and participation in other cultural activities. There are no prerequisites for this program."
    url = "https://www.southwestern.edu/study-abroad/study-abroad-programs/su-amsterdam/index.php"

    #all relationships will be lists to accomdiate multiple entries
    areas = ["Computer Science", "Communication"]
    terms = ["Summer 1"]
    languages = ["Dutch"]
    locations = [["Amsterdam", "Netherlands"]]    #This will be a list of list like [city name, country name] representing a location

    create_new_program(providerName, programName, com, res, intern, cost, cost_stipulations, description, url, areas, terms, languages, locations)


    #-----------------------------TEST PROGRAM # 2-------------------------------
    providerName = "B2"
    programName = "SU Buenos Aires" 
    com = False 
    res = True
    intern = True
    cost = "$6,045 - $6,625"
    cost_stipulations = "Schooling Only"
    description = "The program begins with an on-site orientation in Buenos Aires. Students will attend sessions on cultural adaptation host family living, transportation, and safety while also visiting some of Buenos Aires’ most important sites. Organized excursions will include tours of several Buenos Aires neighborhoods, a bike tour, Argentine tango classes, cooking class, and a visit to MALBA, the Latin American Art Museum of Buenos Aires. One of the highlights of the program will be a two-day excursion to the city of Iguazú to view the waterfalls along the border between Argentina and Brazil. Students will also take an overnight trip to an estancia. Classes: SPA15-314:  Conversation in Context (taught by a local instructor) AND SPA15 - 354: Cultures of Latin America (taught by Dr. Carlos De Oro) "
    url = "https://www.southwestern.edu/study-abroad/su-buenos-aires-program/"

    #all relationships will be lists to accomdiate multiple entries
    areas = ["Spanish"]
    terms = ["Summer 1"]
    languages = ["Spanish"]
    locations = [["Buenos Aires", "Argentina"]]    #This will be a list of list like [city name, country name] representing a location

    create_new_program(providerName, programName, com, res, intern, cost, cost_stipulations, description, url, areas, terms, languages, locations)



    #-----------------------------TEST PROGRAM # 3-------------------------------
    providerName = "C3"
    programName = "SU European Cultural Exploration" 
    com = False
    res = True
    intern = False
    cost = "TBD"
    cost_stipulations = NULL
    description = "Courses TBD"
    url = "https://www.southwestern.edu/study-abroad/study-abroad-programs/su-european-cultural-exploration/"

    #all relationships will be lists to accomdiate multiple entries
    areas = ["Mathamatics"]
    terms = ["Summer 2"]
    languages = [NULL]
    locations = [["Lisbon", "Portugal"], ["Grenoble", "France"], ["Budapest", "Hungary"]]    #This will be a list of list like [city name, country name] representing a location

    create_new_program(providerName, programName, com, res, intern, cost, cost_stipulations, description, url, areas, terms, languages, locations)



    #-----------------------------TEST PROGRAM # 4-------------------------------
    providerName = "D4"
    programName = "SU Granada" 
    com = True 
    res = True
    intern = True
    cost = "$5,970 -$6,970"
    cost_stipulations = "All Included"
    description = "The program begins with a thorough orientation in Granada. Students will stay in a hotel their first night, and attend sessions on cultural adaptation and safety while also visiting some of Granada’s most important sites. They will then finish orientation by learning about host family living before meeting their host families and moving into their housing. The final session the following morning will cover the cultural events and excursions that the students will attend as part of the Granada program. Organized excursions will include a weekend trip to Cadiz (including a Panoramic tour with guide, and a visit to Torre Tavira and Museo Fenicio). Then, at the end of the program, the whole group will travel to Madrid and spend their last two days exploring the city together (including a guided walking tour of central Madrid, and a visit to Reina Sofia, Prado Museum, and El Escorial Monastery). Courses: Spanish II - SPA15-154 AND Spanish III - SPA15-164. One course will be taught by SU faculty Dr. Laura Senio Blair and one course will be taught by a local instructor. "
    url = "https://www.southwestern.edu/study-abroad/study-abroad-programs/granada-program/"

    #all relationships will be lists to accomdiate multiple entries
    areas = ["Spanish"]
    terms = ["Summer 1"]
    languages = ["Spanish"]
    locations = [["Granada", "Spain"]]    #This will be a list of list like [city name, country name] representing a location

    create_new_program(providerName, programName, com, res, intern, cost, cost_stipulations, description, url, areas, terms, languages, locations)



     #-----------------------------TEST PROGRAM # 5-------------------------------
    providerName = "E5"
    programName = "SU London" 
    com = False 
    res = False
    intern = False
    cost = NULL
    cost_stipulations = "Equal to Southwestern’s on-campus tuition, room, and board charges for the fall semester of the academic year during which the program is run"
    description = "Students will participate in several local cultural excursions in London throughout the semester.  Previous activities and excursions have included: a backstage tour of the West End Theatre, a guided tour of the Globe Exhibition, cream tea, attendance at the Tower of London Key Ceremony, attendance at a professional soccer (football) game, and a tour of the British Museum. Day trips or overnight trips to the following locations are also cultural components of the program: Bath and Cambridge.  The day trip to Cambridge trip includes round-trip bus transportation and a guided tour of the city. The overnight trip to Bath includes round-trip bus transportation, a guided tour, and admission to Stonehenge. Additionally, students participate in a two-night/three-day field trip to Edinburgh, Scotland.  This field trip includes transportation to and from Edinburgh.  Students share rooms in a hostel on this trip.  Breakfast is included each day.  A visit to the Highland Safari Deer Experience and to the Edinburgh Castle are components of this field trip."
    url = "https://www.southwestern.edu/study-abroad/study-abroad-programs/southwestern-london-program/"

    #all relationships will be lists to accomdiate multiple entries
    areas = ["Physics", "Biology"]
    terms = ["Fall"]
    languages = ["English"]
    locations = [["London", "England"]]    #This will be a list of list like [city name, country name] representing a location

    create_new_program(providerName, programName, com, res, intern, cost, cost_stipulations, description, url, areas, terms, languages, locations)




     #-----------------------------TEST PROGRAM # 6-------------------------------
    providerName = "F6"
    programName = "SU Switzerland" 
    com = False 
    res = False
    intern = True
    cost = "$6,345"
    cost_stipulations = "All Included"
    description = "Excursions Include:  The hike to Monte Bre – This will be a unique mix of urban hike and nature hike that winds through historic sites and ends at the artist’s village of Bre Paese. Dinner at a traditional Ticinese Grotto - Students will be able to experience traditional Ticinese cuisine at a grotto in walking distance of the student residence. On top of Ticino - Afternoon class at the top of Monte Generoso - Students will take a train to Cappolago-Riva S. Vitale where we will then board a cog train to climb Monte Generoso, one of the highest points in Southern Switzerland. There we will have class on the deck of the Mario Botta designed structure, Fiore di Pietra, and walk along the ridgeline to get a panoramic view of Southern Switzerland and Northern Italy where we will discuss Swiss geology, climate, and urban sprawl. And more!"
    url = "https://www.southwestern.edu/study-abroad/study-abroad-programs/su-switzerland/"

    #all relationships will be lists to accomdiate multiple entries
    areas = ["Environmental Studies"]
    terms = ["Summer 1"]
    languages = [NULL]
    locations = [["Lugano", "Switzerland"]]    #This will be a list of list like [city name, country name] representing a location

    create_new_program(providerName, programName, com, res, intern, cost, cost_stipulations, description, url, areas, terms, languages, locations)


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

    


#    fname = "C:\Documents\DataImportFile.txt"
#    lineCount = 1
#    with open(fname, 'r') as f:
#    for eachLine in f:
#    line = eachLine.strip()
#    if(lineCount % 14 == 1):
#    #Provider
#    providerName = line
#
#    if(lineCount % 14 == 2):
#    #Program
#    programName = line
#
#    if(lineCount % 14 == 3):
#    #Community Engagement
#    com = line
#
#    if(lineCount % 14 == 4):
#    #Research Oppurtinities
#    res = line
#
#    if(lineCount % 14 == 5):
#    #Internship Oppurtunities
#    intern = line
#
#    if(lineCount % 14 == 6):
#    #Cost
#    cost = line 
#
#    if(lineCount % 14 == 7):
#    #Cost Stipulations
#    cost_stipulations = line
#
#    if(lineCount % 14 == 8):
#    #Description
#    description = line
#
#    if(lineCount % 14 == 9):
#    #Url
#    url = line
#
#    if(lineCount % 14 == 10):
#    #Areas
#    areas = Convert(line)
#
#    if(lineCount % 14 == 11):
#    #Terms
#    terms = Convert(line)
#
#    if(lineCount % 14 == 12):
#    #Languages
#    languages = Convert(line)
#
#    if(lineCount % 14 == 13):
#    #Locations
#    locations = ConvertLocation(line)
#
#    if(lineCount % 14 == 0): 
#    create_new_program(providerName, programName, cost, com, res,
#                    intern, description, url, areas, terms, languages, locations)
#    lineCount += 1
            


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