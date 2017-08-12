#client
import socket
import select
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_ip = '127.0.0.1'
udp_port = 8010
readList = [client, sys.stdin]
while(True):
    readyToRead, wr, err = select.select(readList , [], [])
    for readFrom in readyToRead:
        if readFrom == sys.stdin:
            message = sys.stdin.readline()
            message = bytearray(message, "utf-8")
            client.sendto(message, (udp_ip, udp_port))
        else:
            reply = client.recvfrom(1000)
            print("Server:%s"%(reply[0]))
        
           
         
      
  
