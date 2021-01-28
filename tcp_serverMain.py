import socket
import random
import time
import datetime
import threading


client_list = []
client_names = []

#/Static Server Settings\#


TCP_Server_main = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ServerMainPort = 557
TCP_Host = "25.53.46.105"
TCP_Server_main.bind((TCP_Host,ServerMainPort))
TCP_Server_main.listen(3)
print("[Server] Server Active Waiting For Connections")
#END






def handle_Client0():
	print("Did something")

	while True:

		client0 = client_list[0].recv(1024).decode("utf-8")
		client_list[1].send(bytes(client0,"utf-8"))


		print(f"Client0: {client0}" )

def handle_Client1():
	print("Did something")

	while True:

		client1 = client_list[1].recv(1024).decode("utf-8")
		client_list[0].send(bytes(client1,"utf-8"))


		print(f"Client1: {client1}")






def handle_Traffic():
	print(client_list)
	print(client_names)

	thread1 = threading.Thread(target=handle_Client0)
	thread2 = threading.Thread(target=handle_Client1)
	thread1.start()
	thread2.start()


def handle_connections():

    while len(client_list) != 2:
	    client_socket , addr = TCP_Server_main.accept()
	    client_list.append(client_socket)
	    client_names.append(client_socket.recv(1024).decode("utf-8"))



    handle_Traffic()

handle_connections()

