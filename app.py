import os
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, g
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, IntegerField
from wtforms.validators import Email, EqualTo, DataRequired, Length, ValidationError

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up!')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class ProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=30)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=30)])
    source = StringField('Source', validators=[DataRequired()])
    refer = StringField('Referred By', validators=[DataRequired()])
    secretQuestion = StringField('Secret Question', validators=[DataRequired()])
    secretAns = StringField('Secret Answer', validators=[DataRequired()])


class EducationForm(FlaskForm):
    grade = StringField('Grade', validators=[DataRequired(), Length(min=4, max=5)])
    major = StringField('Major', validators=[DataRequired()])
    career1 = StringField('Career 1', validators=[DataRequired()])
    career2 = StringField('Career 2', validators=[DataRequired()])
    career3 = StringField('Career 3', validators=[DataRequired()])
    schoolState = StringField('School State', validators=[DataRequired()])
    schoolName = StringField('School Name', validators=[DataRequired()])
    schoolGPA = IntegerField('School GPA', validators=[DataRequired()])
    GPAscale = IntegerField('GPA Scale', validators=[DataRequired()])
    gradDate = StringField('Graduation Date', validators=[DataRequired()])



app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

DATABASE = 'db.sqlite3'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
@app.route('/home')
def index():
	return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)
	if request.method == 'POST':
		return redirect(url_for('login', status="account-created"))

	return render_template('registration.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'POST':
		return redirect(url_for('dashboard', status="user-authenticated"))

	return render_template('login.html', form=form)


@app.route('/application-profile', methods=['GET', 'POST'])
def profile():
	form = ProfileForm(request.form)
	if request.method == 'POST':
		return redirect(url_for('education', status="user-profile"))

	return render_template('application-profile.html', form=form)

@app.route('/application-education', methods=['GET', 'POST'])
def education():
	form = EducationForm(request.form)
	if request.method == 'POST':
		return redirect(url_for('dashboard', status="application-success"))

	return render_template('application-education.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
	return render_template('account.html')


@app.route('/accepted', methods=['GET', 'POST'])
def accepted():
	if request.method == 'POST':
		return redirect(url_for('schedule', status="user-sched"))

	return render_template('account1.html')


@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
	return render_template('schedule.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
	return render_template('chat.html')









