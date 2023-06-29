import sys
import socket

if len(sys.argv) not in [2, 3]:
    print("""Improper number of arguments: at least one is required and not more than two are allowed:
- http server's address (required)
- port number (defaults to 80 if not specified)""")
    exit(1)

# Write your code here.
FORMAT = 'utf-8'
PORT = 80


def request_url(conn_sock):
    conn_sock.send(b'HEAD / HTTP/1.1\r\nHost: ' +
                bytes(url, FORMAT) +
                b'\r\nConnection: close\r\n\r\n')
    reply = conn_sock.recv(10000).decode(FORMAT)
    if reply:
        ip_addr = conn_sock.getpeername()[0]
        print(f'[SUCCESSFUL CONNECTION] Address: {ip_addr} website: {url}')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)





try:
    port = 80 if len(sys.argv) == 2 else int(sys.argv[2])
    url = sys.argv[1]
    address = (url, port)

    sock.connect(address)
    request_url(sock)

except ValueError:
    print('Port number is invalid - exiting.')
    exit(2)

except TimeoutError:
    print('\nFAILED CONNECTION] ****************************')
    print("[TIMED OUT] Connection attempt timed out!\n")
    exit(3)

except Exception as e:
    print('\nFAILED CONNECTION] ****************************')
    print(f'{e} - Exception cause')

else:
    print('HTTP/1.1 302 Found')


