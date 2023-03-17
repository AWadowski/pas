import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect_ex(('127.0.0.1', 2900))
message='kebab'
client.send(message.encode('utf-8'))
print(client.recv(1024).decode('utf-8'))

client.close()