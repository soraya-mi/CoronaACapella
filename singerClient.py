import socket
import time
import sys
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8008)
print("Connecting to server...")
sock.connect(server_address)
#Recieve ack
connection_ack=sock.recv(1024)
print(connection_ack.decode("utf-8"))

#Song file
buf = 1024
SEPARATOR = "<SEPARATOR>"
file_name = 'a.txt'
# get the file size
file_size = os.path.getsize(file_name)
print((12).to_bytes(3, 'big'))

#Send file size
print("Sending file size...")
sock.send(file_size.to_bytes(2, 'big'))
print("File size sended.")
# sock.send(str(file_size).encode())#f"{file_size}".encode()
# print ("Sending %s ..." % file_size)
# print(str(file_size).encode())


#open file
f = open(file_name, "rb")
data = f.read(buf)
while True:
    res=input("Enter: ")
    if res=='end':
        break
    elif res=='send':
        while(data):
            print("Sending file data :")
            if sock.sendto(data, server_address):
                print(data.decode("utf-8"))
                print("data sended.")
                data = f.read(buf)
                time.sleep(0.02) # Give receiver a bit time to save
        sock.close()
        f.close()

# print("Sending data:",data)
# sock.send(data)

# Receive the message back
# res = sock.recv(1024).decode('utf-8')
# print(res)

