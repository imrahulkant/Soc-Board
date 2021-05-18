import socket

newSocket = socket.socket()
sip = input("Enter your ip : ")
port = 8334
newSocket.bind((sip, port))
newSocket.listen(1) 
conn, add = newSocket.accept()

 
while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print("client", ':', message)