import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect_ex(('212.182.24.236', 2908))
message = input()
message = message.ljust(20)[:20]
client.send(message.encode('utf-8'))
data = client.recv(20)
print(data.decode('utf-8'))

client.close()