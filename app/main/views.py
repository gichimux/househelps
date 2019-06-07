from flask import render_template,request,redirect,url_for
from . import main
# from .. import socketio

@main.route('/')
def index():
    return render_template('landing.html')

