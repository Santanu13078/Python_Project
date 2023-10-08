import socket
import sys

try:
    server=socket.socket()
    ip='127.0.0.1'
    port=3999
    server.bind((ip,port))
    server.listen(5)
    print('Server is listening......')
except Exception as e:
    print('Server cannot be created...')
    print(e)
    sys.exit()

while True:
    client,addr=server.accept()
    print(f'Client connected from {addr}')
    while True:
        try:
            data=client.recv(1024)
            print(f'client{(addr)} : {data.decode()}')
            data=input('Enter data to send : ')
            client.send(bytes(data,'utf-8'))
        except Exception as e:
            print(f'Connection is closed ... due to {e}')
            client.close()
            server.close()
