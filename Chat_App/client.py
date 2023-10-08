import socket
import sys

try:
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Client socket created successfully')
except socket.error as err:
    print('Socket Object cannot be created...')
    sys.exit()

print('Enter server details: ')
print('1. Enter server IP')
print('2. Enter server name')
choice=input('Enter your choice: ')
ip=''
if int(choice)==1:
    ip=input('Enter IP address : ')
else:
    try:
        addr=input('Enter host name : ')
        ip=socket.gethostbyname(addr)
    except:
        print('Invalid server address')
        sys.exit()

port=int(input('Enter port number to connect : '))
try:
    client.connect((ip,port))
    print('Connection successfull......')
    while True:
        data=input('Enter data to send : ')
        client.send(bytes(data,'utf-8'))
        data=client.recv(1024)
        print(f'Server : {data.decode()}')
except socket.error as err:
    print(f'Cannot connect to {ip} due to {err}')
client.close()