import sqlite3
import os
import socket
import time

def init_db():
    db = sqlite3.connect('info.db')

    #print "Opened database successfully";

    db.execute('''CREATE TABLE INFO 
       (id        CHAR(20)      NOT NULL,
        longitude  CHAR(20)     NOT NULL,
        latitude   CHAR(20)     NOT NULL,
        time       CHAR(20)     NOT NULL);''')
    print "Table created successfully";
    db.commit()
    db.close()



bind_ip='0.0.0.0'
bind_port=10027    
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((bind_ip,bind_port))


db = sqlite3.connect('info.db')



print "[*]listening on %s : %d"%(bind_ip,bind_port)
while True:
    msg,addr=server.recvfrom(1024)
    print 'received:',msg,'from',addr
    name=msg.split(':')[0]
    longitude=msg.split(':')[1]
    latitude=msg.split(':')[2]
    time_recv=time.strftime('%Y-%m-%d|%Hh%Mm%Ss',time.localtime(time.time()))
    str_cmd='''INSERT INTO INFO (id,longitude,latitude,time)  VALUES ('%s', '%s','%s','%s')'''%(name,longitude,latitude,time_recv)
    print str_cmd
    db.execute(str_cmd);
    db.commit()


    
    



            
        
    
