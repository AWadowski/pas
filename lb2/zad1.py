import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect_ex(('ntp.task.gda.pl', 13))
print(client.recv(1024).decode('utf-8'))
client.close()