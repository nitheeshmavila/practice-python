#server
import socket
import sys
import select

udp_ip = '127.0.0.1'
udp_port = 8010
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((udp_ip,udp_port))
readersList = [server, sys.stdin]
while True:
    readyToRead, readyToWrite, error = select.select(readersList, [], [])
   
    for readFrom in readyToRead:
        if readFrom == server:
            r = server.recvfrom(1000)
            client_address = r[1]
            print("client : %s"%(r[0]))
            reply = sys.stdin.readline()
            reply = bytearray(reply, "utf-8")
            server.sendto(reply, client_address)
    

