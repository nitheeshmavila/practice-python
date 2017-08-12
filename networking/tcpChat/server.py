#server
import socket
tcp_ip = '127.0.0.1'
tcp_port = 8027
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((tcp_ip, tcp_port))
server.listen(1)
connection, clientAddress = server.accept()
while True:
    r = connection.recvfrom(1000)
    print("client : %s"%(r[0]))
    reply = input('server : ')
    reply = bytearray(reply, "utf-8")
    connection.sendto(reply, clientAddress)
    
  


