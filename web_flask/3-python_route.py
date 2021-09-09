#!/usr/bin/python3
"""starts flask web app"""

from flask import Flask
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

app.run(host='0.0.0.0', port=5000)
