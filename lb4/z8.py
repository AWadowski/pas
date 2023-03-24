import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ifopen = client.connect_ex(('127.0.0.1', 2900))

if ifopen == 0:
    print('connected')
    message1 = '1'
    message2 = '2'
    client.send(message1.encode('utf-8'))
    client.send("-".encode('utf-8'))
    client.send(message2.encode('utf-8'))
    data = b''
    while len(data) < 20:
        try:
            packet = client.recv(20 - len(data))
            if not packet:
                break
            data += packet
        except:
            break
    if len(data) == 20:
        print('received message:', data.decode('utf-8'))
    else:
        print('error: received message has incorrect length')
else:
    print("connection lost")
client.close()
