import socket

socketServer = socket.socket()
sip = input("Enter Server ip : ")
sport = 8334

name = input('Enter Your name: ')

socketServer.connect((sip, sport))

socketServer.send(name.encode())
server_name = socketServer.recv(1024)
server_name = server_name.decode()
 
print(server_name,' has joined...')

while True:
    message = (socketServer.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("Me : ")
    socketServer.send(message.encode())