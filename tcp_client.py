import socket
import random
import time
import datetime
import threading
import pyautogui
#/Static Client Settings\#

TCP_Client_main = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ServerMainPort = 557
TCP_Host = "25.53.46.105"
TCP_Client_main.connect((TCP_Host,ServerMainPort))

#END

def main_function(user):
	TCP_Client_main.send(bytes(user,"utf-8"))

	def recieve_message():
		while True:

			message = TCP_Client_main.recv(1024).decode("utf-8")

			print("\n")
			print(f"[INCOMMING] : {message}")



	def send_message():
		while True:

			message_TCP = str(input("Message: "))
			TCP_Client_main.send(bytes(message_TCP,"utf-8"))



	recieve_thread = threading.Thread(target=recieve_message)
	send_thread = threading.Thread(target=send_message)
	recieve_thread.start()
	send_thread.start()





def login_Screen():
	print("############################################################################")
	print("Please Log In")
	username = str(input("user: "))
	print("################################## Logged In ###############################")
	main_function(username)


login_Screen()