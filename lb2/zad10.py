import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect_ex(('212.182.24.236', 2907))
message = input("hostname")
client.send(message.encode('utf-8'))
data = client.recv(1024)
print(data.decode('utf-8'))
    
client.close()