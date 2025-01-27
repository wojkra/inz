from iec104client import *
from iec104_tcp_packets import *

server_ip = '192.168.30.200'
client = iec104_tcp_client(server_ip)
#test = client.sendOne(p)
for p in plist:
    print client.sendOne(p)
