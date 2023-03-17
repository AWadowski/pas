import sys
import socket

try:
    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])
    else:
        print("Za malo argumentow")
    for port in range(1, 65535):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        client.connect_ex((target, port))
        print(f"Port {port} jest otwarty")
        print(socket.getservbyport('127.0.0.1','tcp'))
        client.close()
except socket.gaierror:
    print("hostname error")
except socket.error:
    print("else error")