import socket
def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5566  # initiate port no above 1024
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    # configure how many client the server can listen simultaneously

    message, address = server_socket.recvfrom(2048)
    # accept new connection
    print("Connection from: " + str(address))
    print(str(message))
    server_socket.sendto(str("this connection is ok ").encode(), address)
    counter = 0
    while True:
        data, address = server_socket.recvfrom(2048)
        if not data:
            break
        print("counter is : " + str(data))
        counter += 1
        server_socket.sendto(str(counter).encode(), address)
    server_socket.close()
if __name__ == '__main__':
    server_program()