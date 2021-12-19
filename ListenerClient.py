import socket
import binascii
import struct

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# try:
#     sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# except AttributeError:
#     pass
# sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
# sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)

sock.bind(('', MCAST_PORT))
host = socket.gethostbyname(socket.gethostname())
print(host)
# sock.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(host))
# sock.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP,socket.inet_aton(MCAST_GRP) + socket.inet_aton(host))
group = socket.inet_aton(MCAST_GRP)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
while 1:
    try:
      data, addr = sock.recvfrom(1024)
    except socket.error as e:
        print ('Expection')
        hexdata = binascii.hexlify(data)
        print ('Data = %s' % hexdata)
