#client program
import select
import sys
import socket

UDP_IP="127.0.01"
UDP_PORT=6003

def prompt() :
	sys.stdout.write('<Client> ')
	sys.stdout.flush()

def client():
	client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	print 'Connected to remote host. Start sending messages '
	prompt()
	while True:
		rlist,wlist,elist=select.select([client_socket,sys.stdin],[],[])
		for sock in rlist:
			if sock is sys.stdin:
				msg=sys.stdin.readline()
				client_socket.sendto(msg,(UDP_IP,UDP_PORT))
				prompt()
			elif sock is client_socket:
				data,addr=client_socket.recvfrom(1024)
				print '< Mesage from server > ',
				sys.stdout.write(data)
				prompt()
			
	client_socket.close()
client()
