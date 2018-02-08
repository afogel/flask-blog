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

if __name__ == '__main__':
	app.run(debug=True)