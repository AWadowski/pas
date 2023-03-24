import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 9214))

while True:
    data, address = sock.recvfrom(1024)
    decoded_data = data.decode("utf-8")
    ip_address = socket.gethostbyname(decoded_data)
    sock.sendto(ip_address.encode("utf-8"), address)
