from socket import *

import os.path
# reserve port 7788 on the computer
serverPort = 7788
# *The SOCK_STREAM: connection-oriented TCP protocol.
serverSocket = socket(AF_INET, SOCK_STREAM)
# Associates the socket with its local address, allowing clients to connect to the server using that address.
serverSocket.bind(("", serverPort))
# Set the socket to listening mode, where 1 represents the number of incoming connections.
serverSocket.listen(1)
print("The Server is Ready!")
# Infinite loop until it interrupted or an error occurs
while True:
    # accept() is called by the server to accept or complete the connection.
    connection_Socket, address = serverSocket.accept()
    # Receive data from the server and decode it to obtain the string.
    sentence = connection_Socket.recv(1024).decode()
    print(address)
    print(sentence)
    ip = address[0]
    port = address[1]
    request = sentence.split()[1]
    request = request.lower()
    request = request.lstrip('/')  
    # If the request is / or index.html then send the main html file to the client
   # if request == "/" or request == "/index.html":
    if request == '' or request == 'index.html' or request == 'main_en.html' or request == 'en': # If the requested file is index.html or index or empty then send the index.html file to the client.
        # Open the requested file
        requestedFile = open("main_en.html")
        # Read the requested file
        webPage = requestedFile.read()
        # Close the requested file after getting the data from it
        requestedFile.close()
        # Send the response status to the client after encoding it to the byte type
        connection_Socket.send("HTTP/1.1 200 OK\r\n".encode())
        # send the type of the file after encoding it to the byte type
        connection_Socket.send("Content-Type: text/html \r\n".encode())
        # send CRLF(new line) to the client after encoding it to the byte type
        connection_Socket.send("\r\n".encode())
        # send the requested file that we read before to the client
        connection_Socket.send(webPage.encode())

    elif request == 'main_ar.html' or request == 'ar': # If the requested file is  main_ar.html or index or empty then send the index.html file to the client.
        requestedFile = open("main_ar.html")
        webPage = requestedFile.read()
        requestedFile.close()
        connection_Socket.send("HTTP/1.1 200 OK\r\n".encode())
        connection_Socket.send("Content-Type: text/html ;charest=utf-8\r\n".encode())
        connection_Socket.send("\r\n".encode())
        connection_Socket.send(webPage.encode())

        # If the request ends with .css then send the Cascading Style Sheet:"style.css" to the client
    elif request.endswith(".css"):
        requestedFile = open("style.css")
        webPage = requestedFile.read()
        requestedFile.close()
        connection_Socket.send("HTTP/1.1 200 OK\r\n".encode())
        connection_Socket.send("Content-Type: text/css \r\n".encode())
        connection_Socket.send("\r\n".encode())
        connection_Socket.send(webPage.encode())
        # If the request ends with .html then send java script code: used in the main html code
    elif request.endswith(".html"):
        requestedFile = open(request)
        webPage = requestedFile.read()
        requestedFile.close()
        connection_Socket.send("HTTP/1.1 200 OK\r\n".encode())
        connection_Socket.send("Content-Type: text/css \r\n".encode())
        connection_Socket.send("\r\n".encode())
        connection_Socket.send(webPage.encode())
    elif request.endswith(".jpg"): 
        requestedFile = open(request , "rb")
        webPage = requestedFile.read()
        requestedFile.close()
        connection_Socket.send("HTTP/1.1 200 OK\r\n".encode())
        connection_Socket.send("Content-Type: image/jpg \r\n".encode())
        connection_Socket.send("\r\n".encode())
        connection_Socket.send(webPage)
        # If the request ends with .jpeg then send image code to the client
    elif request.endswith(".jpeg"):
        requestedFile = open(request, "rb")
        webPage = requestedFile.read()
        requestedFile.close()
        connection_Socket.send("HTTP/1.1 200 OK\r\n".encode())
        connection_Socket.send("Content-Type: image/jpeg \r\n".encode())
        connection_Socket.send("\r\n".encode())
        connection_Socket.send(webPage)
            # If the request ends with .png then send image code to the client
    elif request == "go":
        connection_Socket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connection_Socket.send("Content-Type: text/html \r\n".encode())
        connection_Socket.send("Location:https://www.google.com \r\n".encode())
        connection_Socket.send("\r\n".encode())
    elif request == "so":
        connection_Socket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connection_Socket.send("Content-Type: text/html \r\n".encode())
        connection_Socket.send("Location:https://www.stackoverflow.com \r\n".encode())
        connection_Socket.send("\r\n".encode())
    elif request == "bzu":
        connection_Socket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
        connection_Socket.send("Content-Type: text/html \r\n".encode())
        connection_Socket.send("Location:https:/ritaj.birzeit.edu/ \r\n".encode())
        connection_Socket.send("\r\n".encode())
                 
    # If the request doesn't end with the mentioned above, then send the notfound file
    else:
        ST = ('<head> <title>Error</title></head><head><style>body { background-image: url("back.jpg"); background-repeat: no-repeat;'
'background-attachment: fixed;background-size: 100% 100%;}</style></head><body> <h1 style="color:red">The file is not found</h1><br>'
'<h2 style="color:black">Tala Abahra 1201002</h2><h2 style="color:black">Maha Mali 1200746</h2><p style="color:black">'
'<p><b>Client IP:'+str(address[0])+'</b></p><p><b>Client PORT:'+str(address[1])+'</b></p></body></html>').encode('utf-8')
        connection_Socket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connection_Socket.send("Content-Type: text/html \r\n".encode())
        connection_Socket.send("\r\n".encode())
        connection_Socket.send(ST)
        # Close the connection
    connection_Socket.close()