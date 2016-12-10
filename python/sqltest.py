import sqlite3


conn = sqlite3.connect('demo.db')

c= conn.cursor()

c.execute('''CREATE TABLE users (username tesxt, email text)''')
c.execute("INSERT INTO users VALUES ('me', 'me@mydomain.com')")

conn.commit()

username, email = 'me', 'me@mydomain.com'

c.execute("INSERT INTO users VALUES (?, ?)", (username, email) )

userlist = [
	('paul', 'paul@gmail.com'),
	('donny', 'donny@gmail.com'),
]

c.executemany("INSERT INTO users VALUES (?, ?)", userlist)


conn.commit()

username = 'me'

c.execute('SELECT email FROM users WHERE username = ?', (username, ))

print c.fetchone()

lookup = ('me',)
c.execute('SELECT email FROM users WHERE username = ?', lookup )
print c.fetchone()


#Connect to mySQL database -> yum install MySQL-python
import MySQLdb

conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="")
c = conn.cursor()
c.execute("CREATE DATABASE testdb ")

c.execute("USE testdb ")

c.execute ("CREATE TABLE users (username VARCHAR(50), email VARCHAR(50) ) ")

userlist = [
	('paul', 'paul@gmail.com'),
	('donny', 'donny@gmail.com'),
]

c.executemany("INSERT INTO users VALUES (%s, %s)", userlist )

conn.commit()
c.execute("SELECT * FROM users")

for row in c.fetchall():
	print row

conn.close()
