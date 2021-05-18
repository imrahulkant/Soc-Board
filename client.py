import socket
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

socketServer = socket.socket()
sip = input("Enter Server ip : ")
sport = 8334

name = input('Enter Your name: ')

socketServer.connect((sip, sport))

socketServer.send(name.encode())
server_name = socketServer.recv(1024)
server_name = server_name.decode()


print('[green] {} is Joined . . .[/green]'.format(server_name))

while True:
    message = (socketServer.recv(1024)).decode()
    panel = Text(message, justify="left")
    print("[blue] {} [/blue]".format(panel))
    #print(server_name, ":", message)
    message = Prompt.ask("Type Your Message . . . ")
    socketServer.send(message.encode())