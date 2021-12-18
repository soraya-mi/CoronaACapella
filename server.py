import socket
from threading import Thread
# import udp_server
from datetime import datetime
class server:
    threads = []
    def __init__(self, host, port, timeout=60):
        self.host = host    # Host address
        self.port = port    # Host port
        self.timeout = timeout
        self.sock = None
    def printwt(self, msg):
        ''' Print message with current date and time '''
        current_date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[{current_date_time}] {msg}')
    def run(self):
        self.sock.configure_server()
    def configure_server(self):
        ''' Configure the server '''
        # create TCP socket with IPv4 addressing
        self.printwt('Creating socket...')
        self.printwt('Socket created')
        # bind server to the address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # bind the socket to its host and port
        self.printwt(f'Binding server to {self.host}:{self.port}...')
        self.sock.bind((self.host, self.port))
        self.printwt(f'Server binded to {self.host}:{self.port}')
        # start listening for a client
        self.sock.listen(5)
        while True:
            # get the client object and address
            client, address = self.sock.accept()
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

    # def handle_client(self,):
    #    '''handle client connection'''
