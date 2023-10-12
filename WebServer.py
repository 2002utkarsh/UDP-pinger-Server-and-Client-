#import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)


serverPort = 12000
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

#Prepare a sever socket
#Fill in start
#Fill in end

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:

        message = connectionSocket.recv(1024).decode()  # Fill in start #Fill in end

        filename = message.split()[1]
        f = open(filename[1:])

        outputdata = f.read() #Fill in start #Fill in end

        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"

        connectionSocket.send(response.encode())


        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            
        connectionSocket.close()
    
    
    except IOError:

        not_found_response ="HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<html><head></head><body><h1>404 Not Found</h1></body></html>"
        connectionSocket.send(not_found_response.encode())
       
        connectionSocket.close()

serverSocket.close()
