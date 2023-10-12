from socket import *
from time import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.connect(('localhost', 12000))

