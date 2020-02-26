from fullDatabaseRemake import Admin,areas,terms,cities,languages,Program,Area,Term, City,Country, Language 
from databaseTesting import db



#This file is to be run upon initial setup of the database, and should pull from a 
#backup file inorder to populate new database 

db.create_all()



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
Newprogram = Program("Spain shit", "500",True,True,True,"This is for testing, we wish a study abroad only cost 500")
Newprogram.area=[Area("CS")]
Newprogram.language=[Language("Spanish")]
newCity = City("Madrid")
newCity.countries=[Country("Spain")]
Newprogram.city=[newCity]
Newprogram.term=[Term("Spring")]
db.session.add(Newprogram)
db.session.commit()
