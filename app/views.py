from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = 'House Helps App'
    title = 'Home- Welcome to the House Help application'

    return render_template('index.html', title = title, message = message)


