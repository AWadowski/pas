import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9214))
server.listen(1)

while True:
    connection, address = server.accept()
    print(f"Connected by {address}")

    data = connection.recv(20).decode('utf-8')
    print(f"Received {data}")

    response = data.upper()
    connection.sendall(response.encode('utf-8'))
    print(f"Sent {response}")

    connection.close()
