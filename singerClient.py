import socket
import time
import sys
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8008)
sock.connect(server_address)

###Song file
buf = 1024
SEPARATOR = "<SEPARATOR>"
file_name = 'a.txt'
# get the file size
file_size = os.path.getsize(file_name)
print(file_size)
#send file size


# sock.send(str(file_size).encode())#f"{file_size}".encode()
# print ("Sending %s ..." % file_size)
# print(str(file_size).encode())


#open file
f = open(file_name, "rb")
data = f.read(buf)

while(data):
    print("Sending file data :")
    if sock.sendto(data, server_address):
        print(data.decode("utf-8"))
        data = f.read(buf)
        time.sleep(0.02) # Give receiver a bit time to save
sock.close()
f.close()

# print("Sending data:",data)
# sock.send(data)
print("data sended.")
# Receive the message back
# res = sock.recv(1024).decode('utf-8')
# print(res)

