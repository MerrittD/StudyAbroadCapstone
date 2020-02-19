from db import db
from admin import Admin
from term import Term, programs_terms
from programs import Program
from locations import City, Country, programs_cities, cities_countries
from languages import Language, programs_languages
from areas import Area, programs_areas
db.create_all()

