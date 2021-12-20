import socket
import select

#create sockect
UDP_IP = "127.0.0.1"
IN_PORT = 5005
timeout = 3
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, IN_PORT))


while True:
    #recieve file name

    while True:
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            print(ready)
            print("     Data:")
            data, addr = sock.recvfrom(1024)
            # f.write(data)
            print("     ",data.decode("utf-8"))
        else:
            break