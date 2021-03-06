from flask import Flask, render_template, request, session, flash, redirect, \
	url_for, g
import sqlite3
import secret_key_generator
import pdb # python debugger; to set breakpoint: pdb.set_trace()
from sessions_helper import login_required

# set config variables here
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = secret_key_generator.generate()

app = Flask(__name__)

# pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

# function to connect to the database
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

# Add routes
@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	status_code = 200
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or \
			request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid Credentials. Please try again.'
			status_code = 401
		else:
			session['logged_in'] = True
			return redirect(url_for('main'))
	return render_template('login.html', error=error), status_code

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out.')
	return redirect(url_for('login'))

@app.route('/main')
@login_required
def main():
	g.db = connect_db()
	cursor = g.db.execute('SELECT * FROM posts')
	posts = [dict(title=row[0], post=row[1]) for row in cursor.fetchall()]
	g.db.close()
	return render_template('main.html', posts=posts)

@app.route('/add', methods=['POST'])
@login_required
def add():
	title = request.form['title']
	post = request.form['post']
	if not title or not post:
		flash('All fields are required. Please try again.')
		return redirect(url_for('main'))
	else:
		g.db = connect_db()
		g.db.execute('INSERT INTO posts (title, post) VALUES (?, ?)', [title, post])
		g.db.commit()
		g.db.close()
		flash('New entry was successfully posted.')
		return redirect(url_for('main'))

if __name__ == '__main__':
	app.run(debug=True)