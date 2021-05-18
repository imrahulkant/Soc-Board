import socket

socketServer = socket.socket()
sip = input("Enter your ip : ")
sport = 8334
socketServer.connect((sip, sport))

while True:
    message = (socketServer.recv(1024)).decode()
    print("server_name", ":", message)
    message = input("Me : ")
    socketServer.send(message.encode())