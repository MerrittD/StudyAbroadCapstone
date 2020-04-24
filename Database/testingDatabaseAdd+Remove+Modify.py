from databaseORM import Admin,areas,terms,locations,languages,programs,Program,Area,Term,Location,Language,Provider 
from databaseConfiguration import db

# Written by Luke Yates
# Last Updated: 4/10/2020 


#This file will contain the script to test modification and removal of all classes in databaseORM

#The file "testingDatabaseSetup.py" should be run on an empty database which is contained in the 
#   folder "EmptyDatabase", then this file can be run to modify the existing test database. 

#All information stored in the finished test database is located in a drive excel sheet 
#   named "Dummy Study Abroad Programs Data". 
# https://docs.google.com/spreadsheets/d/1T_cO_Zb0LjXWC506Ji134R-u3nhHM4E-GgsWaxd-maw/edit?usp=sharing


#Everything Tested in the file works. However, when a relationship is removed, it does not check to see 
#   if the entity that had all connections removed stays in the database as it own object, 
#   Therefore the object must be deleted in the future. 
#This is solved in the API methods for changing and removing programs



def main():
    #------------------Remove Actions-----------------
    #Test Language: Remove Spanish from SU Buenos Aires
    Program.find_by_name("SU Buenos Aires").remove_language(Language.find_by_name("Spanish"))
    db.session.commit()

    #Test Loaction: Remove Lisbon, Portugal from SU European Cultural Exploration
    Program.find_by_name("SU European Cultural Exploration").remove_location(Location.find_by_name("Lisbon", "Portugal"))
    db.session.commit()
            #Removed the connection, but didnt remove Lisbon from the database


    #Test Area: Remove Biology from SU London
    Program.find_by_name("SU London").remove_area(Area.find_by_name("Biology"))
    db.session.commit()

    #Test Term: Remove Summer 1 from SU Amsterdam
    Program.find_by_name("SU Amsterdam").remove_term(Term.find_by_name("Summer 1"))
    db.session.commit()


    #------------------Modify Actions-----------------
    #Test removing Description from SU European Cultural Exploration
    Program.find_by_name("SU European Cultural Exploration").description = None
    db.session.commit()

    #Test Changing community engagement learning opportunity to False for SU Amsterdam
    Program.find_by_name("SU Amsterdam").comm_eng = False
    db.session.commit()

    #Test removing provider 
    Provider.find_by_name("A1").remove_program(Program.find_by_name("SU Amsterdam"))
    db.session.commit()
    


    #------------------Add Actions-----------------
    #Add Spanish and French to SU ECE
    languages = ["Spanish", "French"]
    for i in languages:
        if(Language.get_language_id(i) == -1):
            tempLanguage = Language(i)
            tempLanguage.save_to_db()
        else: 
            tempLanguage = Language.find_by_name(i)
        
        Program.find_by_name("SU European Cultural Exploration").add_language(tempLanguage)
        db.session.commit()


if __name__ == '__main__':
    main()