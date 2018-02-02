from flask import Flask, flash, redirect, render_template, request, session, abort 
import os
from flask_sqlalchemy import SQLAlchemy
from flask.ext.session import Session 

app = Flask(__name__)
app.debug=True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
sess = Session()


class Comment(db.Model):
	id = db.Column(db.Integer, primary_key= True, autoincrement=True)
	user = db.Column(db.String(255), nullable=False)
	title = db.Column(db.String(255), nullable=True)
	content = db.Column(db.String(255), nullable=False)

db.create_all()



@app.route('/')
def main():
	return render_template('about.html') 

@app.route('/about')
def about():
	return render_template('about.html') 

@app.route('/management')
def managment():
	return render_template('managment.html')

@app.route('/student')
def student():
	return render_template('student.html')

@app.route('/time')
def time():
	return render_template('time.html')

@app.route('/comments')
def comments():
	comments = Comment.query.order_by(Comment.user).all()
	return render_template('comments.html', comments = comments)

@app.route('/addComment', methods=['POST'])
def addComment():
	if request.method== 'POST':
		comment = Comment()
		comment.user = request.form['name']
		comment.title = request.form['title']
		comment.content = request.form['content']
		db.session.add(comment)
		db.session.commit()

	comments = Comment.query.order_by(Comment.user).all()
	return render_template('comments.html', comments = comments)

@app.route('/deleteComment', methods=['POST'])
def deleteComment():
	if request.method== 'POST':
		id = request.form['id']
		Comment.query.filter(Comment.id == id).delete()
		db.session.commit()

	comments = Comment.query.order_by(Comment.user).all()
	return render_template('comments.html', comments = comments)


if __name__ == "__main__":
	app.secret_key = 'super secret key'
	app.config['SESSION_TYPE'] = 'filesystem'
	sess.init_app(app)
	app.run(debug=True)
