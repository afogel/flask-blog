# Create a SQLite3 table and populate it with data

import sqlite3

with sqlite3.connect('blog.db') as connection:
	# get a cursor object used to excute SQL commands
	c = connection.cursor()

	# create the table
	c.excute('''
		CREATE TABLE posts
		(title TEXT, post TEXT)
		''')

	# insert dummy data into the table
	c.excute('INSERT INTO posts VALUES("Good", "I\'m good."')
	c.excute('INSERT INTO posts VALUES("Well", "I\'m swell."')
	c.excute('INSERT INTO posts VALUES("Excellent", "I\'m excellent."')
	c.excute('INSERT INTO posts VALUES("Merp", "I\'m merp."')
