import sqlite3
db = sqlite3.connect('info.db')
cur=db.execute('select * from info limit 10')
for row in cur:
	print row

