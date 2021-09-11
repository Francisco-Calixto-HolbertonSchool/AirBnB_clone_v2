#!/usr/bin/python3
"""starts flask web app"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def remove_session():
    '''remove the current SQLAlchemy Session after request'''
    storage.close()


@app.route('/states_list')
def states_list():
    '''render html page with a list of states'''
    objs = storage.all(State)
    return (render_template('6-number_odd_or_even.html', objs = objs))


app.run(host='0.0.0.0', port=5000)
