from flask import render_template,request,redirect,url_for
from . import main

@main.route('/')
def index():
    # title = 'welcome to the maid application'
    return render_template('landing.html')

# @main.route()