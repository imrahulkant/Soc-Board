import socket
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

socketServer = socket.socket()
sip = input("\nEnter Server ip : ")
sport = 8334

name = input('\n\nEnter Your name: ')

socketServer.connect((sip, sport))

socketServer.send(name.encode())
server_name = socketServer.recv(1024)
server_name = server_name.decode()


print('\n\n[green] {} is Joined . . .[/green]'.format(server_name))

while True:
    message = (socketServer.recv(1024)).decode()
    panel = Text(message, justify="left")
    print("\n[yellow] {0} [/yellow] : [blue] {1} [/blue]".format(server_name,panel))
    message = Prompt.ask("Type Your Message . . . ")
    socketServer.send(message.encode())