import socket
import time
# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the server IP address and port number
server_address = ('20.121.204.44', 12345)

# connect to the server
client_socket.connect(server_address)

while(True):
# send some data to the server
    message = "Hello, server!"
    client_socket.sendall(message.encode())
    print("sending..")
    time.sleep(2)

# # receive data from the server
# data = client_socket.recv(1024)

# # print the data received from the server
# print("Received from server: ", data.decode())

# close the socket
client_socket.close()
