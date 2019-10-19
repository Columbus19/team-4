from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	user =  'Kamesh'
	return render_template('index.html', user=user)


@app.route('/student')
def students():
	return render_template('undergrads.html')

@app.route('/login')
def login():
	return render_template("login.html")

@app.route('/register')
def register():
	return render_template("register.html")