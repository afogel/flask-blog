# Create a SQLite3 table and populate it with data

import sqlite3

with sqlite3.connect('blog.db') as connection:
	# get a cursor object used to execute SQL commands
	c = connection.cursor()

	c.execute('DROP TABLE IF EXISTS posts')
	# create the table
	c.execute('''
		CREATE TABLE posts
		(title TEXT, post TEXT)
		''')

	# insert dummy data into the table
	c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
	c.execute('INSERT INTO posts VALUES("Well", "I\'m swell.")')
	c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
	c.execute('INSERT INTO posts VALUES("Merp", "I\'m merp.")')
