#!/usr/bin/python3
"""starts flask web app"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """home route"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    "hbnb route"
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_is_etc(text):
    """variable route"""
    return ("C {}".format(text.replace('_', ' ')))


@app.route('/python')
@app.route('/python/<text>', strict_slashes=False)
def python_is_etc(text="is cool"):
    """variable route"""
    return ("Python {}".format(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def reps_int(n):
    """variable route"""
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def templates(n):
    """displays html page only if n is an int"""
    return (render_template('5-number.html', n=n))

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    """displays html if n is int, classifies by even or odd"""
    if (n % 2 == 0):
        return (render_template('6-number_odd_or_even.html', n=n, even=True))
    else:
        return (render_template('6-number_odd_or_even.html', n=n, even=False))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
