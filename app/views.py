from flask import render_template, url_for, flash, redirect
from .forms import RegistrationForm, LoginForm
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

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.firstname.data}!','success')
        return redirect(url_for('index'))
    

    '''
    View root page function that returns the index page and its data
    '''
    
    title = "Sign Up"

    return render_template('register.html', title = title,form=form)


@app.route('/login')
def login():
    form = LoginForm()

    '''
    View root page function that returns the index page and its data
    '''
    
    title = "Login"

    return render_template('login.html', title = title,form=form)



