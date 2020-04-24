from databaseORM import Admin,areas,terms,locations,languages,programs,Program,Area,Term,Location,Language,Provider 
from databaseConfiguration import db




#This file will be to test the methods below taken from the API-WIP and make sure 
#   They modify the database correctly


#This is a generic script to populate an entire new program
#   If a parameter is optional, then pass "None" for the value: cost, cost_stipulations, description, url (optional)
#   If it is meant to be a list, then leave the list empty "[]": areas, terms, languages, locations (optional)
def create_new_program(providerName, programName, com, res, intern, cost, cost_stipulations, description, url, areas, terms, languages, locations): 
    #-----------------------------PROVIDER RELATIONSHIP----------------------------
    # Check if the provider already exist, if it doesn't then make a new provider
    prov = Provider.find_by_name(providerName)
    if(prov == None):
        prov = Provider(providerName)
        prov.save_to_db()

    # Check if the program already exist, if it doesn't then make a new program
    prog = Program.find_by_name(programName)
    if(prog == None):
        prog = Program(programName, com, res, intern, cost, cost_stipulations, description, url)
        prog.save_to_db()  

    #Add the program to the provider
    prov.add_program(prog)
    prov.save_to_db()


    #-----------------------------PROGRAM RELATIONSHIPS----------------------------
    # AREA, TERM, LANGUAGES, LOCATION

    # AREA: 
    # Cyle through all area names: check to see if the area already exist in the db, 
    #    if it doesn't, add it to the program and create the relationship. 
    for i in areas:
        tempArea = Area.find_by_name(i)
        if(tempArea == None):
            tempArea = Area(i)
            tempArea.save_to_db()     
        
        prog.add_area(tempArea)
        prog.save_to_db()
        #might need save to db methods

    # TERM: 
    # Cyle through all term names: check to see if the term already exist in the db, 
    #    if it doesn't, add it to the program and create the relationship. 
    for i in terms:
        tempTerm = Term.find_by_name(i)
        if(tempTerm == None):
            tempTerm = Term(i)
            tempTerm.save_to_db() 
        
        prog.add_term(tempTerm)
        prog.save_to_db()
        #might need save to db methods

    # LANGUAGES: 
    # Cyle through all term names: check to see if the term already exist in the db, 
    #    if it doesn't, add it to the program and create the relationship. 
    for i in languages:
        tempLanguage = Language.find_by_name(i)
        if(tempLanguage == None):
            tempLanguage = Language(i)
            tempLanguage.save_to_db()
        
        prog.add_language(tempLanguage)
        prog.save_to_db()
        #might need save to db methods

    # LOCATION: 
    # Cyle through all term names: check to see if the term already exist in the db, 
    #    if it doesn't, add it to the program and create the relationship. 
    for i in locations:
        tempLocation = Location.find_by_name(i[0], i[1])
        if(tempLocation == None):
            tempLocation = Location(i[0], i[1])
            tempLocation.save_to_db()
                    
        prog.add_location(tempLocation)
        prog.save_to_db()



#This method will define changing or removing any attribute for a specific 
#   program that already exist

#Parameters: 
#   programName- (string) name of program that the languages are being changed for
#   com- (boolean) value of community engagement oppurtunity presence 
#   res- (boolean) value of research oppurtunity presence
#   intern- (boolean) value of internship oppurtunity presence
#   cost- (string) cost of program
#   cost_stipulations- (string) string of stipulations for costs
#   descriptions- (string) description for program
#   url- (string) url of program 
#   
# Any value that is None is unchanged

# Return True if completed
def change_program(programName, com, res, intern, cost, cost_stipulations, description, url): 

    prog = Program.find_by_name(programName)

    if(prog == None):
        raise ValueError

    if(com != None):
        prog.comm_eng = com

    if(res != None):
        prog.research_opp = res

    if(intern != None):
        prog.internship_opp = intern

    if(cost != None):
        prog.cost = cost

    if(cost_stipulations != None):
        prog.cost_stipulations = cost_stipulations

    if(description != None):
        prog.description = description

    if(url != None):
        prog.url = url

    return True



        #This method will define changing or removing a area from a program
#   If it is removing, the front end will pass "remove"
#   If it is adding, the front end will pass "add" for first 
#Parameters: 
#   change- (string: "add" or "remove")  specify desired change to db
#   program- (string) name of program that the areas are being changed for
#   areas- (list) names of areas being added or removed from program
# Return True if completed
def change_or_remove_areas_for_program(change, programName, areas):
    
    prog = Program.find_by_name(programName)

    if(prog == None):
        raise ValueError
    if(areas == []):
        return True

    if(change == "add"):
        for i in areas:
            tempArea = Area.find_by_name(i)

            if(tempArea == None):
                tempArea = Area(i)
                tempArea.save_to_db()

            prog.add_area(tempArea)
            prog.save_to_db()

    elif(change == "remove"):
        for i in areas:
            tempArea = Area.find_by_name(i)

            if(tempArea == None):
                raise ValueError

            prog.remove_area(tempArea)
            prog.save_to_db()

            #This if statement checks to see if the removed Language has any more existing relationships
            #   If there are none, then delete the language from the database 
            if(Areas.query.join(Programs_Areas).filter((Programs_Areas.c.area_id == tempArea.id)).first() == None):
                tempArea.delete()

            prog.save_to_db()
    else:
        raise ValueError

    session.commit()
    return True



#This method will define changing or removing a term from a program
#   If it is removing, the front end will pass "remove"
#   If it is adding, the front end will pass "add" for first 
#Parameters: 
#   change- (string: "add" or "remove")  specify desired change to db
#   program- (string) name of program that the terms are being changed for
#   terms- (list) names of terms being added or removed from program
# Return True if completed
def change_or_remove_terms_for_program(change, programName, terms):
    
    prog = Program.find_by_name(programName)

    if(prog == None):
        raise ValueError
    if(terms == []):
        return True

    if(change == "add"):
        for i in terms:
            tempTerm = Term.find_by_name(i)

            if(tempTerm == None):
                tempTerm = Term(i)
                tempTerm.save_to_db()

            prog.add_term(tempTerm)
            prog.save_to_db()

    elif(change == "remove"):
        for i in terms:
            tempTerm = Term.find_by_name(i)

            if(tempTerm == None):
                raise ValueError

            prog.remove_term(tempTerm)
            prog.save_to_db()

            #This if statement checks to see if the removed Language has any more existing relationships
            #   If there are none, then delete the language from the database 
            if(Term.query.join(Programs_Terms).filter((Programs_Terms.c.term_id == tempTerm.id)).first() == None):
                tempLanguage.delete()

            prog.save_to_db()
    else:
        raise ValueError    #If change is not "add" or "remove"

    session.commit()
    return True



#This method will define changing or removing a language from a program
#   If it is removing, the front end will pass "remove"
#   If it is adding, the front end will pass "add" for first 
#Parameters: 
#   change- (string: "add" or "remove")  specify desired change to db
#   program- (string) name of program that the languages are being changed for
#   languages- (list) names of languages being added or removed from program
# Return True if completed
def change_or_remove_languages_for_program(change, programName, languages):
    
    prog = Program.find_by_name(programName)

    if(prog == None):
        raise ValueError
    if(languages == []):
        return True

    if(change == "add"):
        for i in languages:
            tempLanguage = Language.find_by_name(i)

            if(tempLanguage == None):
                tempLanguage = Language(i)
                tempLanguage.save_to_db()

            prog.add_language(tempLanguage)
            prog.save_to_db()

    elif(change == "remove"):
        for i in languages:
            tempLanguage = Language.find_by_name(i)

            if(tempLanguage == None):
                raise ValueError

            prog.remove_language(tempLanguage)
            prog.save_to_db()

            #This if statement checks to see if the removed Language has any more existing relationships
            #   If there are none, then delete the language from the database 
            if(Languages.query.join(Programs_Languages).filter((Programs_Languages.c.language_id == tempLanguage.id)).first() == None):
                tempLanguage.delete()

            prog.save_to_db()
    else:
        raise ValueError

    session.commit()
    return True



#This method will define changing or removing a location from a program
#   If it is removing, the front end will pass "remove"
#   If it is adding, the front end will pass "add" for first 
#Parameters: 
#   change- (string: "add" or "remove")  specify desired change to db
#   program- (string) name of program that the languages are being changed for
#   locations- (list) names of locations being added or removed from program. List of List in form\
#       [[CityName, CountryName], [CityName, CountryName]]
# Return True if completed
def change_or_remove_locations_for_program(change, programName, locations):
    
    prog = Program.find_by_name(programName)

    if(prog == None):
        raise ValueError
    if(locations == []):
        return True

    if(change == "add"):
        for i in locations:
            tempLocation = Location.find_by_name(i[0], i[1])
            if(tempLocation == None):
                tempLocation = Location(i[0], i[1])
                tempLocation.save_to_db()
                    
            prog.add_location(tempLocation)
            prog.save_to_db()

    elif(change == "remove"):
        for i in locations:
            tempLocation = Location.find_by_name(i[0], i[1])

            if(tempLocation == None):
                raise ValueError

            prog.remove_location(tempLocation)
            prog.save_to_db()

            #This if statement checks to see if the removed Language has any more existing relationships
            #   If there are none, then delete the language from the database 
            if(Locations.query.join(Programs_Locations).filter((Programs_Locations.c.location_id == tempLocation.id)).first() == None):
                tempLocation.delete()

            prog.save_to_db()
    else:
        raise ValueError

    session.commit()
    return True



#This method removes the list of programs from the provided provider and back deletes
# Any unused provider after removing specific methods will be deleted. 
# Parameters: 
#   providerName - (string) name of provider to have programs removed from
#   programs - (list of strings) list of program names that are to be deleted from provider
def remove_programs_from_provider(providerName, programs): 

    prov = Provider.find_by_name(providerName)
    if(prov == None):
        raise ValueError
    
    for i in programs:
        tempProgram = Program.find_by_name(i)

        if(tempProgram == None):
            raise ValueError

        prov.remove_location(tempProgram)
        prog.save_to_db()

    
    #This if statement checks to see if the resulting Provider has any more existing relationships
    #   If there are none, then delete the provider from the database 
    if(Providers.query.join(Programs_Providers).filter((Programs_Providers.c.provider_id == prov.id)).first() == None):
        prov.delete()

    session.commit()
    return True



# This method removes a program from the database, 
#       all back updates to other tables are carried out
# Paramter: 
#   - programName: (string) name of the program to be deleted
def remove_program(programName):

    prog = Program.find_by_name(programName)

    if(prog == None):
        raise ValueError

    locations = []
    for i in prog.location:
        locations.append(list(i.city, i.country))

    terms = []
    for i in prog.term:
        terms.append(i.name)

    languages = []
    for i in prog.language:
        languages.append(i.name)

    areas = []
    for i in prog.area:
        areas.append(i.name)

    change_or_remove_locations_for_program("remove", programName, locations)
    change_or_remove_terms_for_program("remove", programName, prog.term)
    change_or_remove_languages_for_program("remove", programName, prog.language)
    change_or_remove_areas_for_program("remove", programName, prog.area)

    #check for provider to see if there are any more programs and delete if not. 
    prov = Providers.query.join(Programs_Providers).filter((Programs_Providers.c.program_id == prog.id)).first()
    if(prov != None):
        remove_programs_from_provider(prov, list(programName))

    prog.delete()

    session.commit()

    return True








def main():
    setup = False

    if(setup == True):
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
        description = "The program begins "
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
        cost_stipulations = None
        description = "Courses TBD"
        url = "https://www.southwestern.edu/study-abroad/study-abroad-programs/su-european-cultural-exploration/"

        #all relationships will be lists to accomdiate multiple entries
        areas = ["Mathamatics"]
        terms = ["Summer 2"]
        languages = []
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
        description = "The program begins with a thorough orientation in Granada. "
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
        cost = None
        cost_stipulations = "Equal to "
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
        description = "Excursions Include"
        url = "https://www.southwestern.edu/study-abroad/study-abroad-programs/su-switzerland/"

        #all relationships will be lists to accomdiate multiple entries
        areas = ["Environmental Studies"]
        terms = ["Summer 1"]
        languages = []
        locations = [["Lugano", "Switzerland"]]    #This will be a list of list like [city name, country name] representing a location

        create_new_program(providerName, programName, com, res, intern, cost, cost_stipulations, description, url, areas, terms, languages, locations)


         #-----------------------------TEST PROGRAM # 7-------------------------------
         #This is not listed on google drive dummy data, but it is to test remove program 
        providerName = "G7"
        programName = "Remove Test" 
        com = False 
        res = False
        intern = True
        cost = "$6,000"
        cost_stipulations = "All Included"
        description = "Excursions Include:  "
        url = "www.com"

        #all relationships will be lists to accomdiate multiple entries
        areas = ["Environmental Studies", "Biology", "AreaToBeRemoved"]
        terms = ["Summer 1", "TermToBeRemoved"]
        languages = ["Spanish", "LanguageToBeRemoved"]
        locations = [["Lugano", "Switzerland"], ["CityToBeRemoved", "CountryToBeRemoved"]]    #This will be a list of list like [city name, country name] representing a location

        create_new_program(providerName, programName, com, res, intern, cost, cost_stipulations, description, url, areas, terms, languages, locations)

    else: 
        #Run testing script
        remove_program("Remove Test")
        #When setup is false above, then the modifiying code can run. 

    



if __name__ == '__main__':
    main()
