import socket
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

newSocket = socket.socket()
sip = input("Enter Client ip : ")
port = 8334
newSocket.bind((sip, port))

print( "Binding successful!" )
print("This is your IP: ", sip)

name = input('Enter Your name: ')

newSocket.listen(1) 
conn, add = newSocket.accept()

client = (conn.recv(1024)).decode()
print('[green] {} is Online . . .[/green]'.format(client))

conn.send(name.encode())

while True:
    message = Prompt.ask("Type Your Message . . . ")
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    panel = Text(message, justify="left")
    print("[blue] {} [/blue]".format(panel))
    #print(client, ':', message)