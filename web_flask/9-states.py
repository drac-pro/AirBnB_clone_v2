#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """list all states or all cities in a state"""
    states = storage.all(State)
    if state_id:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def closedb_session(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
