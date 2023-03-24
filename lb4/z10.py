import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 2909)
server.bind(server_address)

while True:
    print('Waiting for a message...')
    data, address = server.recvfrom(1024)
    print(f"Received {len(data)} bytes from {address}")
    
    try:
        data_str = data.decode('utf-8')
        parts = data_str.split()
        if len(parts) < 3:
            raise ValueError("Incomplete message")
        source_port = int(parts[0], 16)
        dest_port = int(parts[1], 16)
        message = "".join([chr(int(x, 16)) for x in parts[32:]])
        if message.strip() == "hello :)":
            response = "TAK"
        else:
            response = "NIE"
    except ValueError as e:
        print(f"Error: {e}")
        response = "BADSYNTAX"
        
    server.sendto(response.encode('utf-8'), address)
