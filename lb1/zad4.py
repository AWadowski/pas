import socket

ip_address = input("Podaj IP: ")
try:
    hostname = socket.gethostbyaddr(ip_address)[0]
    print(f"hostname dla {ip_address} to {hostname}.")
except socket.herror:
    print(f"brak hostname {ip_address}.")