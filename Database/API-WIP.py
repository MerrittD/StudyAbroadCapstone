"""
Routes and views for the flask application.
"""

from databaseORM import Admin,Programs_Areas,Programs_Terms,Programs_Locations,Programs_Languages,Programs_Providers,Program,Area,Term,Location,Language,Provider 
from databaseConfiguration import app, db
from flask import render_template,request, jsonify, Flask
import flask
import json

# API Written by Daniel Merritt and Luke Yates
# additional help from Alyssa Case
#   Last updated: 4/28/2020

#app = Flask(__name__)
app.config["DEBUG"] = True

#psuedo code from book for api
#might need to do one for each page,
#need to look more into this
#so we'll need one for the admin dash, admin login
#browse, and result
@app.route('/', methods=['GET'])
def home():
    providers = Provider.return_all_providers()
    json_list=[i.serialize for i in providers]
    return  jsonify(json_list)


@app.route('/results', methods=['GET'])
def results():
    # the following values are taken from the get request and can be used to filter
    #if null, dont filter by it
    languageRequest = flask.request.values.get('lan')
    locationRequestCity = flask.request.values.get('loccity')
    locationRequestCountry = flask.request.values.get('loccountry')
    areaRequest = flask.request.values.get('area')
    termRequest = flask.request.values.get('term')
    #providerRequest = flask.request.values.get('prov')str' object has no attribute '_sa_instance_state

    #the following handles the presence of multiple values per param by
    #splitting them into an array. all values are strings
    langArray = []
    locArray=[]
    areaArray=[]
    termArray=[]
    if languageRequest is not None:
        langArray = languageRequest.split(',')
    if locationRequestCity is not None:
        locArray=[[locationRequestCity,locationRequestCountry]]
    if areaRequest is not None:
        areaArray = areaRequest.split(',')
    if termRequest is not None:
        termArray = termRequest.split(',')


    #https://stackoverflow.com/questions/27810523/sqlalchemy-elegant-way-to-deal-with-several-optional-filters used for reference below
    #here the arrays of values are taken and used to filter the database query before returning it
    toQuery = db.session.query(Programs_Areas, Programs_Terms, Programs_Locations, Programs_Languages, Programs_Providers, Area, Term, Location,Program, Language)
    print("Past toQuery")
    if languageRequest is not None:
        for lang in langArray:
            language = Language.find_by_name(lang)
            toQuery = toQuery.filter(Programs_Languages.c.language_id == language.id)
            print(lang)
    if locationRequestCity is not None:
        for loc in locArray:
            location = Location.find_by_name(loc[0],loc[1])
            toQuery = toQuery.filter(Programs_Locations.c.location_id == location.id)
    if areaRequest is not None:
        for a in areaArray:
            area = Area.find_by_name(a)
            toQuery = toQuery.filter(Programs_Areas.c.area_id == area.id)
    if termRequest is not None:
        for t in termArray:
            term = Term.find_by_name(t)
            toQuery = toQuery.filter(Programs_Terms.c.term_id== term.id)
    
    toQuery = toQuery.all()
    # all items returned are converted to a json object and returned 
    json_results=[i.serialize for i in toQuery]
    print(json_results)
    return jsonify(json_results)

    #provArray = providerRequest.split(',')
    #http://127.0.0.1:5000/results?loc=Spain,Madrid&lan=Spanish 
    # /request = approute 
    #? = query 
    #loc=Spain,Madrid = the location is sent two or more locatons using ,. These could be grouped using (Spain Madrid)
    #& is used to add another value 

     # here should be the methods to filter
     #the filters should go through each array and use them for the filter inputs 
     #these should be put in a variable called filterResults

     #Message for Daniel: use this webiste to nest queries. 
     # https://medium.com/shoprunner/multi-table-filters-in-sqlalchemy-d64e2166199f


    #after results are gathered
    #json_list = [i.serialize for i in filterResults]
    return jsonify(langArray)

    return 

@app.route('/login',methods=['GET','PUT'])
def login():
    #methods might be needed here to log in fully. 
    return None

#checking verbs of incoming request
@app.route('/admin', methods=['GET','POST', 'PUT', 'DELETE'])
def check():
    if request.method == 'GET':
       results()

    elif request.method == 'POST':
        #use post to update
        originalName = flask.request.values.get('originalName')
        addOrRemoveLang = flask.request.values.get('langPar')
        addOrRemoveTerm= flask.request.values.get('termPar')
        addOrRemoveArea= flask.request.values.get('areaPar')
        addOrRemoveLoc= flask.request.values.get('locPar')
        updateJson  = flask.request.get_json(force=True)
        # each new update variable will be named and received in a simmilar fasion. It will look messy
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #AJ, Look into using a json for this. look into the flask request api
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
       
        #These are all the possible things that can be updated. If null, it wont be changed or removed
        print(originalName)
        print(updateJson)
        print(type(updateJson))
        updateName= None
        updateComm= None
        updateResearch= None
        updateIntern= None
        updateCost= None
        updateStipulations= None
        updateDesc= None
        updateUrl= None
        updateArea= None
        updateLang= None
        updateLocCity= None
        updateLocCountry =None
        updateTerm= None
        updateProvider = None

        if 'upname' in updateJson:
            updateName=updateJson['upname']
        if 'upcom' in updateJson:
            updateComm=updateJson['upcom']
        if 'upre' in updateJson:
            updateResearch=updateJson['upre']
        if 'upin' in updateJson:
            updateIntern=updateJson['upin']
        if 'upcos' in updateJson:
            updateCost=updateJson['upcos']
        if 'upsti' in updateJson:
            updateStipulations=updateJson['upsti']
        if 'updesc' in updateJson:
            updateDesc=updateJson['updesc']
        if 'upurl' in updateJson:
            updateUrl=updateJson['upurl']
        if 'uplang' in updateJson:
            updateLang=updateJson['uplang']
        if 'uploccit' in updateJson:
            updateLocCity=updateJson['uploccit']
        if 'uploccou' in updateJson:
            updateLocCountry=updateJson['uploccou']
        if 'upter' in updateJson:
            updateTerm=updateJson['upter']
        if 'uparea' in updateJson:
            updateArea=updateJson['uparea']
        if 'upprov' in updateJson:
            updateProvider=updateJson['upprov']
        updateAreas = updateArea.split(',')
        updateTerms =updateTerm.split(',')
        updateLanguages = updateLang.split(',')
        updateCities = updateLocCity.split(',')
        updateCountries = updateLocCountry.split(',')
        updateLocations = []
        for i in range(0,len(updateCities)):
            updateCountry.append([str(updateCities[i]),str(updateCountries[i])])
            
        #find the program
        programToModify = Program.find_by_name(originalName)
        #modify the selected values with data given
        #data will be in the variables and should be type cast as needed. 
        addOrRemoveLang = flask.request.values.get('langPar')
        addOrRemoveTerm= flask.request.values.get('termPar')
        addOrRemoveArea= flask.request.values.get('areaPar')
        addOrRemoveLoc= flask.request.values.get('locPar')

        change_program(originalName, updateComm, updateResearch, updateIntern, updateCost, updateStipulations, updateDesc, updateUrl)
        change_or_remove_areas_for_program(addOrRemoveArea, originalName, updateAreas)
        change_or_remove_terms_for_program(addOrRemoveTerm, originalName, updateTerms)
        change_or_remove_languages_for_program(addOrRemoveLang, originalName, updateLanguages)
        change_or_remove_locations_for_program(addOrRemoveLoc,originalName, updateLocations)

       


        #update modified date

        return (str(orioriginalName) + " modified")

        # if the program is successfully modified 
            #return jsonify("success")
        #else, return either a message saying it failed or render the page with an error sent 

    elif request.method == 'PUT':
        updateJson  = flask.request.get_json(force=True)
        # each new update variable will be named and received in a simmilar fasion. It will look messy
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #AJ, Look into using a json for this. look into the flask request api
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
       
        #These are all the possible things that can be updated. If null, it wont be changed or removed
        updateName= None
        updateComm= None
        updateResearch= None
        updateIntern= None
        updateCost= None
        updateStipulations= None
        updateDesc= None
        updateUrl= None
        updateArea= None
        updateLang= None
        updateLocCity= None
        updateLocCountry =None
        updateTerm= None
        updateProvider = None

        if 'upname' in updateJson:
            updateName=updateJson['upname']
        if 'upcom' in updateJson:
            updateComm=updateJson['upcom']
        if 'upre' in updateJson:
            updateResearch=updateJson['upre']
        if 'upin' in updateJson:
            updateIntern=updateJson['upin']
        if 'upcos' in updateJson:
            updateCost=updateJson['upcos']
        if 'upsti' in updateJson:
            updateStipulations=updateJson['upsti']
        if 'updesc' in updateJson:
            updateDesc=updateJson['updesc']
        if 'upurl' in updateJson:
            updateUrl=updateJson['upurl']
        if 'uplang' in updateJson:
            updateLang=updateJson['uplang']
        if 'uploccit' in updateJson:
            updateLocCity=updateJson['uploccit']
        if 'uploccou' in updateJson:
            updateLocCountry=updateJson['uploccou']
        if 'upter' in updateJson:
            updateTerm=updateJson['upter']
        if 'uparea' in updateJson:
            updateArea=updateJson['uparea']
        if 'upprov' in updateJson:
            updateProvider=updateJson['upprov']
        updateAreas = updateArea.split(',')
        updateTerms =updateTerm.split(',')
        updateLanguages = updateLang.split(',')
        updateCities = updateLocCity.splut(',')
        updateCountries = updateLocCountry.split(',')
        updateLocations = []
        for i in range(0,len(updateCities)):
            updateCountry.append([updateCities[i],updateCountries[i]])
        
        create_new_program(updateProvider, updateName, updateComm, updateResearch, updateIntern, updateCost, updateStipulations, updateDesc, updateUrl, updateAreas, updateTerms, updateLanguages, updateLocations)

        return "Program added"
    elif request.method == 'DELETE':

        #given the id of a program, delete it from database
        programName= flask.request.values.get('progname')
       
        #take in the id and use that to delete 
        remove_program(programName)
        return ("Program: " + str(programName)+ " Deleted")


# A route to return all of the available entries in our catalog.
#@app.route('/api/v1/resources/books/all', methods=['GET'])
#def api_all():
#    return jsonify(books)

if True:
    app.run()







# The methods below are as follows (for Daniel's Use): 

#   1.   create_new_program(programName(string), com(boolean), res(boolean), intern(boolean), 
#                           cost(string), cost_stipulations(string), description(string), url(string) 
#                           areas(list:strings), terms(list:strings), languages(list:strings), locations(list:strings))

#   2.   change_program(programName(string), com(boolean), res(boolean), intern(boolean), 
#                       cost(string), cost_stipulations(string), description(string), url(string))

#   3.   change_or_remove_areas_for_program(change(string: "add" or "remove"), program(string), areas(list:strings))
#   4.   change_or_remove_terms_for_program(change(string: "add" or "remove"), program(string), terms(list:strings))
#   5.   change_or_remove_languages_for_program(change(string: "add" or "remove"), program(string), languages(list:strings))
#   6.   change_or_remove_locations_for_program(change(string: "add" or "remove"), program(string), locations(list:strings))

#   7.   remove_programs_from_provider(providerName(string), programs(list: strings))
#   8.   remove_program(programName(string))

#Notes: 
#  - A remove_provider method is unnecessary becasue the programs will not be deleted so there is nothing to back update. 
#  - All back removal of unused languages, locations, terms, areas, and providers will be deleted. 
#  - It was a design decision that a progam should only be removed with a remove program method call. 
#  - If the method calls for a parameter, but that parameter does not need to be changed, then pass
#       "None" in it's place for a single data type and an [](empty list) for any parameter that is a list
#       and the parameter will be ignored. 

#  - For future develoupment: come of the methods below could be moved to the database with a little bit of recoding. 

#  - The methods below were tested using the file named testAPImethods.py They were copied and pasted 
#       becasue API-WIP is not a valid python file name so they had to be copied instead of imported. 


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

    prog.save_to_db()
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
            if(Area.query.join(Programs_Areas).filter((Programs_Areas.c.area_id == tempArea.id)).first() == None):
                db.session.delete(tempArea)

            prog.save_to_db()
    else:
        raise ValueError

    db.session.commit()
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
                db.session.delete(tempTerm)

            prog.save_to_db()
    else:
        raise ValueError    #If change is not "add" or "remove"

    db.session.commit()
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
            if(Language.query.join(Programs_Languages).filter((Programs_Languages.c.language_id == tempLanguage.id)).first() == None):
                db.session.delete(tempLanguage)

            prog.save_to_db()
    else:
        raise ValueError

    db.session.commit()
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
            if(Location.query.join(Programs_Locations).filter((Programs_Locations.c.location_id == tempLocation.id)).first() == None):
                db.session.delete(tempLocation)

            prog.save_to_db()
    else:
        raise ValueError

    db.session.commit()
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

        prov.remove_program(tempProgram)
        prov.save_to_db()

    
    #This if statement checks to see if the resulting Provider has any more existing relationships
    #   If there are none, then delete the provider from the database 
    if(Provider.query.join(Programs_Providers).filter((Programs_Providers.c.provider_id == prov.id)).first() == None):
        db.session.delete(prov)

    db.session.commit()
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
        locations.append([i.city, i.country])

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
    change_or_remove_terms_for_program("remove", programName, terms)
    change_or_remove_languages_for_program("remove", programName, languages)
    change_or_remove_areas_for_program("remove", programName, areas)

    #check for provider to see if there are any more programs and delete if not. 
    prov = Provider.query.join(Programs_Providers).filter((Programs_Providers.c.program_id == prog.id)).first()
    if(prov != None):
        remove_programs_from_provider(prov.name, [programName])

    db.session.delete(prog)

    db.session.commit()

    return True



#Refrences Used: 
# https://stackoverflow.com/questions/41270319/how-do-i-query-an-association-table-in-sqlalchemy