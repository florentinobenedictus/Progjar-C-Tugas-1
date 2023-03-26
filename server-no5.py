import sys
import socket
import logging

logging.basicConfig(level=logging.INFO)

try:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)

    # Bind the socket to the port
    server_address = ('0.0.0.0', 32444) #--> gunakan 0.0.0.0 agar binding ke seluruh ip yang tersedia

    logging.info(f"starting up on {server_address}")
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)
    #1 = backlog, merupakan jumlah dari koneksi yang belum teraccept/dilayani yang bisa ditampung, diluar jumlah
    #             tsb, koneks akan direfuse
    while True:
        # Wait for a connection
        logging.info("waiting for a connection")
        connection, client_address = sock.accept()
        logging.info(f"connection from {client_address}")
        # Receive the data in small chunks and retransmit it
#         while True:
#             data = connection.recv(32)
#             #32 -> merupakan buffersize, jumlah maksimum data yang bisa diterima sekaligus
#             #buffersize lebih baik diset dalam power of 2 contoh: 1024,32,4096
#             logging.info(f"received {data}")
#             if data:
#                 logging.info("sending back data")
#                 connection.sendall(data)
                
#                 # Read and send file to client
                
                
#             else:
#                 #print >>sys.stderr, 'no more data from', client_address
#                 #print(f"no more data from {client_address}")
#                break
            
        file = open('./server_files/server-file.txt', 'rb')
        line = file.read(1024)
        while(line):
            connection.send(line)
            line = file.read(1024)
            logging.info(line)
        file.close()
        print('sent file to client')
        x = 0
        while(x < 100000000):
            x = x + 1
            if(x % 10000000 == 0):
                logging.info('waiting...')
            continue

        # Clean up the connection
        connection.close()
except Exception as ee:
    logging.log(f"ERROR: {str(ee)}")
finally:
    logging.log('closing')