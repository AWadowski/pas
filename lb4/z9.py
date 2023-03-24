import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 2910))

while True:
    try:
        data, address = server.recvfrom(1024)
        received = data.decode('utf-8')
        if received.startswith('zad14odp;src;') and received.endswith(';data;fun'):
            server.sendto(b'TAK', address)
        else:
            server.sendto(b'NIE', address)
    except:
        server.sendto(b'BADSYNTAX', address)
