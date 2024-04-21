#!/usr/bin/python3
""" a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """simple flask web page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():i
    """simple flask web page"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
