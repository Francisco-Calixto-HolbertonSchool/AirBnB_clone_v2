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
def C(text):
    """variable route"""
    return ("C " + text.replace('_', ' '))

app.run(host='0.0.0.0', port=5000)
