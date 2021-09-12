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


@app.route('/states', strict_slashes=False)
def states_list():
    '''render html page with a list of states'''
    objs = storage.all(State)
    return (render_template('7-states_list.html', navigation=objs))


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id=None):
    '''render html page with a list of states and its cities'''
    objs = storage.all(State)
    for state in objs.values():
        if state.id == id:
            name = state
            valid = True
            break
    return (render_template('9-states.html', state=name, valid=valid))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
