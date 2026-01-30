from socket import *

server_name = "localhost"
server_port = 12000
# Create an internet family(IPv6) socket for datagram transmission.
client_socket = socket(AF_INET6, SOCK_DGRAM)
# Create a timeout to avoid infinitely hanging in case of server failure, etc.
client_socket.settimeout(5)

message = input("Lowercase message: ") # Awaiting console input.
client_socket.sendto(message.encode(), (server_name, server_port))

try:
    modified_message, server_address = client_socket.recvfrom(2048)
    # Varifies the message sent.
    print("From server:", modified_message.decode())
except timeout:
    # In case of server failure...
    print("No response from server.")
client_socket.close()
