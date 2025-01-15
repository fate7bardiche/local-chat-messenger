import socket
import os
from faker import Faker
import faker_wrapper
import json

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

config = json.load(open('config.json'))
server_address = config['filepath']

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('{}でセッションを開始します。'.format(server_address))

sock.bind(server_address)

sock.listen(1)


fake = Faker('jp-JP')

while True:
    connection, client_addres  = sock.accept()
    connection.sendall("helpと入力すると、用意されているデータ名を表示します".encode())

    try:
        while True:
            data = connection.recv(32)

            if not data:
                print("クライアントが接続を切りました")
                break

            data_str = data.decode()
            print(repr(data_str) + 'を受け取りました')

            if(data_str == "help"):
                fake_data_name_text_list = faker_wrapper.fakeDataNameTextList()
                connection.sendall(fake_data_name_text_list.encode())
                continue

            response = faker_wrapper.getValue(fake, data_str)
            print(f"{response}を返します")

            connection.sendall(response.encode())
    except socket.error as err:
        print(err)
        break
    finally:
        print("connectionを閉じます")
        connection.close()
        break

sock.close()
print('接続終了')

 