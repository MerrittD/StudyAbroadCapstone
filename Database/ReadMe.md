# Database Configuration, Database ORM, and API
The code in this directory is the sister code to the front-end designed in this repository. 
For a larger overview of the porject, refer to the overall project's ReadMe in the parent directory to this one. 


## Setup
IDE and Python Distribution 
Links: https://visualstudio.microsoft.com/vs/ use the community version 
           https://docs.conda.io/en/latest/miniconda.html use python 3.7


Instructions: 
First, download and install miniconda. This is a python distribution that also includes helpful libraries and commands for the command prompt.
Once installed, run the conda prompt as an admin and type: 
### `conda install python=3.7.6`
This will install the correct version of python. Then type in the following commands for the libraries.
### `pip install Flask`
### `pip install Flask-SQLAlchemy`

Once these are installed, install visual studio from the link above. When asked what to install with it, choose the python, node.js and webdev options at the top. Then let it install. 

Once everything is installed, clone the project from github and open it in VS. Choose the anaconda environment and you can begin coding 


Database and SQLite setup
Links: 
 - https://dbeaver.io/download/ choose the community version
 - https://sqlite.org/index.html download the latest version


Instructions: 
Follow these directions to setup SQLite: https://www.tutorialspoint.com/sqlite/sqlite_installation.htm
http://johnatten.com/2014/12/07/adding-and-editing-path-environment-variables-in-windows/

DBever will have instructions, just use sqlite

Once a SQL database is located is the same file as the "DatabaseConfiguration.py" and DatabaseORM.py, then commands
can be run to create tables and interact with it. 



## How to Create Tables 
A flask app is created and starts and instance of a SQLAlchemy object stored as "db" which includes all methods for 
changing the database. All tables are defined in the ORM and once they are written, the the command below is used to 
physically allocate memory for them. 
### `db.create_all()` 
### `db.session.commit()` 


## Interactions with the Database
All interactions with the database will be handled by the API and sent from the front-end. Therefore, all 
interactions have been preprogrammed in the API and while filtering, simple methods are called which 
actually change the database. 



## Files

 - README.md: This document
 - API-WIP.py: contains code for front-end information filtering 
 - DatabaseORM.py: Contains table definitions for all tables in the database
 - DatabaseConfiguration.py: sets up the SQLAlchemy object to use the library. 
- PreviousDatabaseTests: contains many databases that were used during testing. Each database is in a different state 
				            depending on what was being tested.   
 

## Known Issues

All classes in the database ORM function as intended. The API works in all cases excpet when quering by
multiple values. This was close to being solved, but there is an error with the joins when querying under the results
section of the API. 


## Author

**Luke Yates and Daniel Merritt**