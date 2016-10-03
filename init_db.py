import sqlite3

db=sqlite3.connect('info.db')
sql="""CREATE TABLE info
       (id CHAR(20),
       	latitude CHAR(20),
       	longitude CHAR(20),
       	time CHAR(20),
	count integer primary key autoincrement);"""

db.execute(sql)
db.commit()
db.close()
