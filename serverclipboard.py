import pyperclip as pc
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cip = input("\nEnter Client ip : ")
port = 8889
client.bind((cip, port))


client.listen(1) 
conn, add = client.accept()

while True:
    message = conn.recv(1024)
    message = message.decode()
    print("\nData Recived...")
    print("\n\t {}".format(message))