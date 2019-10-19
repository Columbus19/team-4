import os
from flask import Flask, render_template, request, url_for, flash, redirect
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
    partOrFull = StringField('Part or Full Time', validators=[DataRequired()])
    major = StringField('Major', validators=[DataRequired()])
    abroad = StringField('Study Abroad or Summer or Both', validators=[DataRequired(), Length(min=4, max=10)])
    career1 = StringField('Career 1', validators=[DataRequired()])
    career2 = StringField('Career 2', validators=[DataRequired()])
    career3 = StringField('Career 3', validators=[DataRequired()])
    schoolState = StringField('School State', validators=[DataRequired()])
    schoolName = StringField('School Name', validators=[DataRequired()])
    schoolGPA = IntegerField('School GPA', validators=[DataRequired()])
    GPAscale = IntegerField('GPA Scale', validators=[DataRequired()])
    gradDate = StringField('Graduation Date', validators=[DataRequired()])


# class QuestionForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up!')

# class DemoForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up!')


# class AddForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up!')

# class AgreeForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up!')


# class ResumeForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up!')


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


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
		return redirect(url_for('profile', status="user-authenticated"))

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
		return redirect(url_for('index', status="user-education"))

	return render_template('application-education.html', form=form)




















	return render_template('login.html', form=form)
