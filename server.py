import socket
from threading import Thread
# import udp_server
from datetime import datetime
class server:
    threads = []
    complet_file='' \
                 '' \
                 ''
    def __init__(self, host, port, timeout=120):
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
    def configure_server(self):
        ''' Configure the server '''
        # create TCP socket with IPv4 addressing
        self.printwt('Creating socket...')
        self.printwt('Socket created.')
        # bind server to the address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # bind the socket to its host and port
        self.printwt(f'Binding server to {self.host}:{self.port}...')
        self.sock.bind((self.host, self.port))
        self.printwt(f'Server binded to {self.host}:{self.port}')
        # start listening for a client
        self.sock.listen(5)
        while self.count<2:
            # get the client object and address
            client, address = self.sock.accept()
            print(address)
            # addr=','.join(address)
            self.printwt("client "+str(address[0])+":"+str(address[1])+" accepted.")
            # set a timeout
            client.settimeout(self.timeout)
            # start a thread to listen to the client
            Thread(target=self.listenToClient, args=(client, address)).start()
            # send the client a connection message
            # res = {
            #     'cmd': 'connected',
            # }
            # response = dumps(res)
            # client.send(response.encode('utf-8'))
    def listenToClient(self, client, address):
        self.printwt("Listening for client "+str(self.count)+" ...")
        # set a buffer size ( could be 2048 or 4096 / power of 2 )
        size = 1024
        while True:
            try:
                self.printwt("Receiving data from the client.")
                # try to receive data from the client
                data = client.recv(size).decode('utf-8')
                if data:
                    self.printwt("Data recieved:", data)
                    # data = loads(data.rstrip('\0'))
                    # send a response back to the client
                    # res = "Hello from server"
                    # response = dumps(res)
                    # print(res)
                    # client.send(res.encode('utf-8'))
                    # print("res sended")
                else:
                    raise error('Client disconnected')
            except:
                self.count+=1
                self.printwt("Connection ended")
                client.close()
                return False
    def multicast(self,):
       '''multicast song to listeners'''


#main
server('127.0.0.1', 8008, timeout=86400).run()