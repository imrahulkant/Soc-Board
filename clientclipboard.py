import pyperclip as pc
import socket
from rich import print

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sip = input("\nEnter Server ip : ")
sport = 8889

host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)

print( "\n\nBinding successful!" )
print("This is Client IP: ", sip)
print("This is Your IP: ", ip)

server.connect((sip,sport))

print( "\n\nClipboard Not Shared Yet .... \n" )

while True:
    data = "No data in clipboard"
    if pc.paste()=="" or pc.paste()==None:
        data = pc.waitForPaste()
    else:
        data = pc.waitForNewPaste()
    server.send(data.encode())
    print("\t [blue] Clipboard Shared... [/blue] \n")