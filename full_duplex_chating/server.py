#server program using select
import socket
import select
import sys
UDP_IP="127.0.01"
UDP_PORT=6003

def prompt() :
        sys.stdout.write('<Server> ')
        sys.stdout.flush()

def server():
	server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	server_socket.bind((UDP_IP,UDP_PORT))
	print 'Waiting for client .....'
	while True:
		rlist,wlist,elist=select.select([server_socket,sys.stdin],[],[])
		for sock in rlist:
			if sock is server_socket:
				data,addr=server_socket.recvfrom(1024)
				print ' <Message from client > ',
				sys.stdout.write(data)
				prompt()
			elif sock is sys.stdin:
				msg=sys.stdin.readline()
				server_socket.sendto(msg,addr)
				prompt()
	server_socket.close()
server()


