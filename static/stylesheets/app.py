from flask import Flask, flash, redirect, render_template, request, session, abort 
import os
from flask_sqlalchemy import SQLAlchemy
#from flask.ext.session import Session 

app = Flask(__name__)
app.debug=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
#sess = session()

class Users(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True);
	email = db.Column(db.String(100), nullable=False);
	password = db.Column(db.String(40), nullable=False);

db.create_all()

@app.route('/login_page')
def login_signup():
	return render_template('login.html')
@app.route('/sign_page', methods=['GET', 'POST'])

def sign_up():
	if request.method=='POST':
		user = Users()
		user.email = request.form['email']
		user.password = request.form['password']
		db.session.add(user)
		db.session.commit()
		return render_template('home.html', user=user) 
	elif request.method=='GET':
		return render_template('login.html')

@app.route('/about')
def about():
	return render_template('about.html') 

@app.route('/management')
def managment():
	return render_template('managment.html')

'''
@app.route('/sign_page', methods=['GET', 'POST'])
def login():
	if request.method=='GET': 
		return render_template('about.html', email=email, password=password)
	elif request.method== 'POST':
		user = db.session.query(Users.filter_by(email=request.form['email']).first())
		if user.password == request.form.get('password'):
			sess('logged_in') = True
			return render_template('about.html', user=user) 
		else: 
			flash('wrong password!!')
			return render_template('login.html')
'''

if __name__ == "__main__":
	app.run(debug=True)