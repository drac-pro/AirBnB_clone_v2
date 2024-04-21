#!/usr/bin/python3
"""Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """simple flask web page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """simple flask web page"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """simple flask web page"""
    text = text.replace('_', ' ')
    return 'C ' + text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
