import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect_ex(('212.182.24.236', 2908))
message = input()
if len(message) < 20:
    message = message.ljust(20)
chunks = [message[i:i+20] for i in range(0, len(message), 20)]
result = ""
for chunk in chunks:
    client.send(message.encode('utf-8'))
    data = client.recv(20)
    result += data.decode('utf-8')
print(result)

client.close()