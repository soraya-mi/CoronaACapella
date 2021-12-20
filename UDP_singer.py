import socket
import time
import sys
import os
from pip._vendor.distlib.compat import raw_input

#create socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

print(f"[+] Sending to {UDP_IP}:{UDP_PORT}")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:             # Loop continuously
    inp = raw_input()   # Get the input
    if inp == "":       # If it is a blank line...
        break           # ...break the loop
    sock.sendto(str.encode(inp), (UDP_IP, UDP_PORT))
    print(inp, "Sended")