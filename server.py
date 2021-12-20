import socket
from threading import Thread,Timer
from datetime import datetime
# import network

threads=[]
song=[]

class TCP_server:
    def __init__(self, host, port, timeout=60):
        self.host = host    # Host address
        self.port = port    # Host port
        self.timeout = timeout
        self.count=1
        self.sock = None

    def printwt(self, msg):
        ''' Print message with current date and time '''
        current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[{current_date_time}] {msg}')

    def run(self):
        self.configure_server()

        if self.count>2:
            print("asfksavfk")
        #     print("in if")
            # r = Timer(5.0, print("1.0s"))
            # r = Timer(1.0, self.multicast())
            # self.multicast()

    def configure_server(self):
        ''' Configure the server '''
        # create TCP socket with IPv4 addressing
        self.printwt('Creating socket...')

        # bind server to the address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.printwt('Socket created.')

        # bind the socket to it's host and port
        self.printwt(f'Binding server to {self.host}:{self.port}...')
        self.sock.bind((self.host, self.port))
        self.printwt(f'Server binded to {self.host}:{self.port}')
        print('\n')

        # start listening for a client
        self.sock.listen(5)
        while self.count<2:

            # get the client object and address
            client, address = self.sock.accept()
            self.printwt("client "+str(address[0])+":"+str(address[1])+" accepted.")

            # set a timeout
            client.settimeout(self.timeout)

            #send ack to client
            self.printwt("Sending connection ack to client...")
            client.send(b"Connection accepted");

            # start a thread to listen to the client
            t=Thread(target=self.listenToClient, args=(client, address))
            threads.append(t)
            t.start()

        # print("Listening ended.")#؟؟؟

    def listenToClient(self, client, address):

        #Listenign to client
        self.printwt("Listening for client "+str(self.count)+" ...")

        #Recieving file size
        self.printwt("Recieving file size ...")
        file_size_byte=client.recv(1024)
        file_size=int.from_bytes(file_size_byte, "big")
        self.printwt("file Size: "+str(file_size))

        while True:
            try:
                # try to receive data from the client
                self.printwt("Receiving data from client...")
                data = client.recv(file_size+5).decode('utf-8')
                song.append(data)

                if data != None:
                    self.printwt("Data recieved:  "+ data)
                    complete_file += str(data)

                else:
                    raise error('Client disconnected.')
            except:
                client.close()

                self.printwt("Connection of client "+str(self.count)+" ended.")
                self.count += 1
                print('\n')
                print(song)
                print(''.join(song))
                # threads[self.count].join()
                # for t in threads:
                    # print(t)
                # print(self.count)
                # print(threads[self.count-1])
                return False
                break

class multicast_UDO_server:
    def __init__(self, MCAST_GRP, MCAST_PORT, timeout=60):
        self.MCAST_GRP = MCAST_GRP    # Host address
        self.MCAST_PORT = MCAST_PORT    # Host port
        self.timeout = timeout
        self.sock = None

    def run(self):
        self.configure_server()

    def Aggregation(self):
        print(''.join(song))

    def configure_server(self,):
       '''multicast song to listeners'''
       MCAST_GRP = '224.1.1.1'
       # MCAST_PORT = 5007
       self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
       self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
       self.sock.sendto(b'Hello Multicast!', (self.MCAST_GRP,self.MCAST_PORT))

       # sta = network.WLAN(network.STA_IF)
       # sta.active(True)
       # sta.connect('ESSID', 'key')
       #
       # # Enabling STA_IF is not enough, as the AP interface continues to run and MicroPython
       # # treats it as the default interface and sends all multicast packets using it.
       # # Disabling it forces the multicast packets to get sent over the STA interface.
       # # See https://github.com/micropython/micropython/issues/2198
       # ap = network.WLAN(network.AP_IF)
       # ap.active(False)
       #
       # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
       # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
       # s.bind(('', 1900))
       # s.sendto(b'some unicast data', ('your-local-machine-ip', 1900))
       # s.sendto(b'some multicast data', ('239.255.255.250', 1900))
#main
TCP_server('127.0.0.1', 8008, timeout=86400).run()
print("after run")
# multicast_UDO_server('239.255.42.99',5007).run()
