#client
import socket
fd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_ip = '127.0.0.1'
udp_port = 8023
while(True):
    message = input("Client :")
    message = bytearray(message, "utf-8")
    fd.sendto(message, (udp_ip, udp_port))
    reply = fd.recvfrom(1000)
   # reply = str(reply)
    print("Server:%s"%(reply[0]))
    
