#server
import socket
udp_ip = '127.0.0.1'
udp_port = 8023
fd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
fd.bind((udp_ip,udp_port))
while True:
    r = fd.recvfrom(1000)
    print("client : %s"%(r[0]))
    reply = input('server : ')
    reply = bytearray(reply, "utf-8")
    client_address = r[1]
    fd.sendto(reply, client_address)
    
  












  

