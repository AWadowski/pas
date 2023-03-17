import socket
import sys


if len(sys.argv) > 1:
    server = sys.argv[1]
    server_ip = socket.gethostbyname(server)
    port = int(sys.argv[2])

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    connection = sock.connect_ex((server_ip, port))
    if connection == 0:
        print("connected")
    else:
        print("not connected")