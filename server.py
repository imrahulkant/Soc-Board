import socket

newSocket = socket.socket()
sip = input("Enter Client ip : ")
port = 8334
newSocket.bind((sip, port))

print( "Binding successful!" )
print("This is your IP: ", sip)

name = input('Enter Your name: ')

newSocket.listen(1) 
conn, add = newSocket.accept()

print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0])

client = (conn.recv(1024)).decode()
print(client + ' is Online . . .')

conn.send(name.encode())

while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)