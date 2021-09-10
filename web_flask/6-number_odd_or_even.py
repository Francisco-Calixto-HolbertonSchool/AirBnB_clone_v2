#!/usr/bin/python3
"""starts flask web app"""

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """home route"""
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    "hbnb route"
    return ("Hello HBNB!")


@app.route('/c/<text>')
def c_is_etc(text):
    """variable route"""
    return ("C {}".format(text.replace('_', ' ')))

@app.route('/python')
@app.route('/python/<text>')
def python_is_etc(text="is cool"):
    """variable route"""
    return ("Python {}".format(text.replace('_', ' ')))


@app.route('/number/<n>')
def reps_int(n):
    """variable route"""
    try:
        n = int(n)
        return ("{} is a number".format(n))
    except:
        pass


@app.route('/number_template/<n>')
def templates(n):
    """displays html page only if n is an int"""
    try:
        n = int(n)
        return (render_template('5-number.html', n = n))
    except:
        pass


@app.route('/number_odd_or_even/<n>')
def even_or_odd(n):
    """displays html if n is int, classifies by even or odd"""
    try:
        n = int(n)
        if (n % 2 == 0):
            return (render_template('6-number_odd_or_even.html', n = n, even = True))
        else:
            return (render_template('6-number_odd_or_even.html', n = n, even = False))
    except:
        pass

app.run(host='0.0.0.0', port=5000)
