import socket
import time 
target_host="103.212.33.238"
target_port=10027

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
	
	client.sendto("dyl:30.50:114.33",(target_host,target_port))
	time.sleep(2)
