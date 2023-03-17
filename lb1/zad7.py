import sys
import socket

try:
    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])
    else:
        print("Za malo argumentow")
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} jest otwarty")
        s.close()
except socket.gaierror:
    print("hostname error")
except socket.error:
    print("else error")