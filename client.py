import socket
import sys
import json

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

config = json.load(open('config.json'))
server_address = config['filepath']

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    sock.settimeout(1)
    initial_data = sock.recv(128)
    print(initial_data.decode())
except socket.error as err:
    pass


while True:
    try: 
        message = input()

        if(message == "exit"):
            break
    
        print(repr(message.encode()) + 'を送ります')
        sock.sendall(message.encode())

        sock.settimeout(2)

        try:
            responses = sock.recv(1024)
            print('serverからの戻り値は以下です')
            print(responses.decode('utf-8'))
        except socket.error as err:
            print(err)
            exit(1)
   
    except socket.error as err:
        print(err)
        sock.close()

sock.close()



