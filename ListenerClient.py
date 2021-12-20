import socket
import binascii
import struct

MCAST_GRP = '239.255.42.99'
MCAST_PORT = 5007
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# try:
#     sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# except AttributeError:
#     pass
# sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
# sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)

sock.bind(('', MCAST_PORT))
host = socket.gethostbyname(socket.gethostname())
print(host)

#--
mreq = struct.pack('4sl', socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
  print(sock.recv(1024))
#--
# sock.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(host))
# sock.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP,socket.inet_aton(MCAST_GRP) + socket.inet_aton(host))
# group = socket.inet_aton(MCAST_GRP)
# mreq = struct.pack('4sL', group, socket.INADDR_ANY)
# sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
# while 1:
#     try:
#       data, addr = sock.recvfrom(1024)
#     except socket.error as e:
#         print ('Expection')
#         hexdata = binascii.hexlify(data)
#         print ('Data = %s' % hexdata)
# import socket
# import struct
#
# MCAST_GRP = '239.255.255.250'
# MCAST_PORT = 1900
#
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.bind((MCAST_GRP, MCAST_PORT))
# mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
# s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
#
# try:
#     while True:
#         print("waiting for data...")
#         data, addr = s.recvfrom(100)
#         print(data, addr)
# except KeyboardInterrupt:
#     pass

s.close()