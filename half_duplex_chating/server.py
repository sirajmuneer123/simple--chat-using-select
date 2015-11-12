#server

import socket

UDP_IP= "127.0.0.1"
UDP_PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
server_socket.bind((UDP_IP, UDP_PORT))
print 'waiting for client.....'

while True:
	data, addr = server_socket.recvfrom(1024)
        print 'Reply from client : ',data
	msg=raw_input('Enter the message : ')
	server_socket.sendto(msg,addr)
server_socket.close()	
