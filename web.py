import os
import sqlite3
from flask import Flask ,request ,session,g,redirect,url_for,abort,render_template,flash
app = Flask(__name__)


@app.route('/')
def show_info():
    
    db = sqlite3.connect('info.db')
    cur = db.execute('select * from info limit 1')
    entries = cur.fetchone()
    db.close()
    return render_template('test1.html' )

@app.route('/getinfo')
def update_info():
	print "enter getinfo"
	name=request.args.get("name")
	db = sqlite3.connect('info.db')
	cur = db.execute('select * from info where id ="%s"order by count desc  limit 1'%name)

	entries = cur.fetchone()
	db.close()
	if entries==None:
		return "none:none:none:none"
	return entries[0]+':'+entries[1]+':'+entries[2]+':'+entries[3]


if __name__=="__main__":
    app.run("0.0.0.0")   
        
        



 





    
