import socket
import sys
import hashlib

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 1234)

try:
    client_socket.connect(server_address)
except socket.error as e:
    print("Error while connecting: {}".format(e), file=sys.stderr)
    sys.exit(1)

print("Connected at:  {}:{}".format(*server_address))

while True:
    message = input("S : ")

    try:
        client_socket.sendall(message.encode())
    except socket.error as e:
        print("Error sending message: {}".format(e), file=sys.stderr)
        sys.exit(1)

    try:
        received_message = client_socket.recv(1024).decode()
    except socket.error as e:
        print("Error receiving message: {}".format(e), file=sys.stderr)
        sys.exit(1)

    print("R : ", received_message)