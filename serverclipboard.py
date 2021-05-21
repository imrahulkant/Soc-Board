import socket
from rich import print
from rich.panel import Panel
from rich.text import Text

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cip = input("\nEnter Client ip : ")
port = 8889
client.bind((cip, port))
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
 

print( "\n\nBinding successful!" )
print("This is Client IP: ", cip)
print("This is Your IP: ", ip)

client.listen(1) 
conn, add = client.accept()

print("\n[bold magenta][*]OK. Clipboard is now shared. Wait... [/bold magenta]\n")

while True:

    message = conn.recv(1024)
    message = message.decode()
    panel = Text(message, justify="left")
    print("\n [green] Data Recived... [green]")
    print("\n\t {}".format(panel))