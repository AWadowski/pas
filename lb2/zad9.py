import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(0.5)
client.connect_ex((socket.gethostbyname("212.182.24.236"), 2906))
client.send('1'.encode('utf-8'))
data = client.recv(1024)
print(data.decode('utf-8'))

client.close()