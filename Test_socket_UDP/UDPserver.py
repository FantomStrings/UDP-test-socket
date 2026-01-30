from socket import *

server_port = 12000
# Create an internet family(IPv6) socket for datagram transmission.
server_socket = socket(AF_INET6, SOCK_DGRAM)
# BInd the socket to host (anywhere) & port.
server_socket.bind(('localhost', server_port))

print("The server is ready to receive...")

while True:
    message, client_address = server_socket.recvfrom(2048)
    print("Received from", client_address, ":", message.decode())
    modified_message = message.decode().upper()
    server_socket.sendto(modified_message.encode(), client_address)
