from socket import *
from time import *

server_name = 'localhost'
port = 12000 

sock = socket(AF_INET, SOCK_DGRAM)
sock.connect((server_name, port))
sock.settimeout(1) 

for i in range(10):
    try:
        start_time = time()
        message = f'Ping {i + 1}'
        sock.send(message.encode())
        data, addr = sock.recvfrom(1024)
        end_time = time()
        rtt = (end_time - start_time) 
        print(f'Received: {data.decode()} from {addr[0]}:{addr[1]}')
        print(f'Round-trip time (RTT): {rtt:.2f} s')
        
    except timeout:
        print('Request timed out')

sock.close()