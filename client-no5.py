import sys
import socket
import logging

#set basic logging
logging.basicConfig(level=logging.INFO)

try:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('172.22.0.5', 32444)
    logging.info(f"connecting to {server_address}")
    sock.connect(server_address)

    # Send data
    # message = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ'
    # logging.info(f"sending {message}")
    # sock.sendall(message.encode())
    # # Look for the response
    # amount_received = 0
    # amount_expected = len(message)
    # while amount_received < amount_expected:
    #     data = sock.recv(16)
    #     amount_received += len(data)
    #     logging.info(f"{data}")
        
    # Create file for file received from server
    file = open('./client_files/received-file.txt', 'wb')
    line = sock.recv(1024)
    logging.info('get following from srv')
    logging.info(line)
    while(line):
        file.write(line)
        line = sock.recv(1024)
        if(line):
            logging.info('yes')
        else:
            logging.info('no')
    file.close()
    print('received file from server')
    x = 0
    while(x < 100000000):
        x = x + 1
        if(x % 10000000 == 0):
            logging.info('waiting...')
        continue
        
except Exception as ee:
    logging.info(f"ERROR: {str(ee)}")
    exit(0)
finally:
    logging.info("closing")
    sock.close()