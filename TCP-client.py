import socket
import threading

ip_master = "placeholder"
port_master = 9999

server = socket.socket(socket.AF_INET, socket,SOCK_STREAM)
server.bind((ip-master,port_master))

def client(client_socket):
	req = client_socket.recv(1024)
	client_socket.send("placeholder")
	{

	}
	client_socket.close()


while True:
	client,adress = server.accept()
	client_handler = threading.Thread(target=client, args=(client,)) 
	client_handler.starte()