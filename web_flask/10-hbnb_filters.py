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


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    '''render html page with a list of states'''
    objs = storage.all(State)
    return (render_template('10-hbnb_filters.html', navigation=objs))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
