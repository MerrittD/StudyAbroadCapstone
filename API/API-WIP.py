"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#psuedo code from book for api
#might need to do one for each page,
#need to look more into this
#so we'll need one for the admin dash, admin login
#browse, and result
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

app.run()