#client
import socket
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_ip = '127.0.0.1'
tcp_port = 8027
try:
    client.connect((tcp_ip, tcp_port))
except:
    print("can't establish connection")
    sys.exit()
while(True):
    message = input("Client :")
    message = bytearray(message, "utf-8")
    client.send(message)
    reply = client.recvfrom(1000) 
    print("Server:%s"%(reply[0]))
    

