import socket
from time import *


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5566  # socket server port number
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # instantiate
    message = "from :maha(1200746) and tala(1201002) "  # take input
    client_socket.sendto(message.encode(), (host, port))  # send message
    print(client_socket.recv(1024).decode())
    num = 0
    while (num < 1000000):
        client_socket.sendto(str(num).encode(), (host, port))  # send message
        data, address = client_socket.recvfrom(2048)
        print("number is: " + str(data))
        num += 1
    print(process_time())
    client_socket.close()  # close the connection
if __name__ == '__main__':
    client_program()