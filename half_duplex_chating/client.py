#client program
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5000

client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print 'connected....' 
while True:
	msg=raw_input('Enter the message : ')
	client_socket.sendto(msg, (UDP_IP, UDP_PORT))
	data, addr=client_socket.recvfrom(1024)
	print 'reply from server : ',data
client_socket.close()
	
	
