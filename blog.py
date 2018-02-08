from flask import Flask, render_template, request, session, flask, redirect, \
	url_for, g
import sqlite3

# set config variables here
DATABASE = 'blog.db'

app = Flask(__name__)

# pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

# function to connect to the database
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

# Add routes
@app.route('/')
def login():
	return render_template('login.html')

@app.route('/main')
def main():
	return render_template('main.html')

if __name__ == '__main__':
	app.run(debug=True)