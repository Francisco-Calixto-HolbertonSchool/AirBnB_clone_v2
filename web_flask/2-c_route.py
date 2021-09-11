#!/usr/bin/python3
"""starts flask web app"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """home route"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    "hbnb route"
    return ("Hello HBNB!")


@app.route('/c/<text>', strict_slashes=False)
def c_is_etc(text):
    """variable route"""
    return ("C {}".format(text.replace('_', ' ')))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
