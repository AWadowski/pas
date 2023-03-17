import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect_ex(('127.0.0.1', 2900))

client.send('1'.encode('utf-8'))
client.send("-".encode('utf-8'))
client.send("2".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))

client.close()