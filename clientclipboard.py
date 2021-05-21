import pyperclip as pc
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sip = input("\nEnter Server ip : ")
sport = 8889

server.connect((sip,sport))

while True:
    data = "No data in clipboard"
    if pc.paste()=="" or pc.paste()==None:
        data = pc.waitForPaste()
    else:
        data = pc.waitForNewPaste()
    server.send(data.encode())