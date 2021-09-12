#!/usr/bin/python3
"""starts flask web app"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def remove_sesh(self):
    '''remove the current SQLAlchemy Session after request'''
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    '''render html page with a list of states and its cities'''
    objs = storage.all(State)
    for state in objs.values():
        print(state.cities)
    return (render_template('7-states_list.html', navigation=objs))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
