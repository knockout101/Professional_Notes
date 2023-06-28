import socket


FORMAT = 'utf-8'
SERVER = input('Input site to send request to: ')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((SERVER, 80))
    client.send(b'GET / HTTP/1.1\r\nHost: ' +
              bytes(SERVER, FORMAT) +
              b'\r\nConnection: close\r\n\r\n')

    print(client.recv(10000).decode(FORMAT))