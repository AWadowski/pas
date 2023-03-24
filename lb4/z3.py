import socket

HOST = '127.0.0.1'
PORT = 9214
BUFFER_SIZE = 1024

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((HOST, PORT))
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            data, address = server_socket.recvfrom(BUFFER_SIZE)
            print(f"Received message from {address}: {data.decode('utf-8')}")
            server_socket.sendto(data, address)

if __name__ == '__main__':
    start_server()
