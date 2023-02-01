import socket
import hashlib

def start_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(('localhost', 1234))

    server_socket.listen(2)

    client1_socket, client1_address = server_socket.accept()
    client2_socket, client2_address = server_socket.accept()

    ip, port = server_socket.getsockname()
    print("UP at: {0}:{1}".format(ip, port))

    while True:
    
        client1_ciphertext = client1_socket.recv(1024)

        if client1_ciphertext.decode().strip() == "closech4t":
            print("closing server")
            client1_socket.close()
            client2_socket.close()
            server_socket.close()
            break

        client2_socket.send(client1_ciphertext)

        client2_ciphertext = client2_socket.recv(1024)

        if client2_ciphertext.decode().strip() == "closech4t":
            print("Bye.")
            client1_socket.close()
            client2_socket.close()
            server_socket.close()
            break

        client1_socket.send(client2_ciphertext)

if __name__ == '__main__':
    while True:
        start_server()