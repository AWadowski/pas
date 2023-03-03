import socket

hostname = input("Wpisz hostname: ")
try:
    ip_address = socket.gethostbyname(hostname)
    print(f"IP dla {hostname} to {ip_address}.")
except socket.gaierror:
    print(f"brak IP dla {hostname}.")