#!/usr/bin/python3
"""flask web application"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
        return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
        return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
        text = text.replace('_', ' ')
        return 'C ' + text

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
        return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
        return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
        return render_template('5-number.html', number=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
	return render_template('6-number_odd_or_even.html', number=n)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
