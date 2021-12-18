import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ('localhost', 8008)
sock.connect(server_address)

# Send the message
d="Hello from client"
sock.sendall(d.encode('utf-8'))
# Receive the message back
print("sff")
# res = sock.recv(1024).decode('utf-8')
# print(res)

