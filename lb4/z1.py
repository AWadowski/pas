import socket
from datetime import datetime

HOST = 'localhost'
PORT = 9214
BACKLOG = 1000
BUFFER_SIZE = 1024

def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(BUFFER_SIZE).decode("utf-8")
            if not data:
                break
            client_socket.sendall(str(datetime.utcnow()).encode("utf-8"))
    except ConnectionResetError:
        pass  # client disconnected
    finally:
        client_socket.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(BACKLOG)
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            client_socket, address = server_socket.accept()
            print(f"Client connected from {address}")
            handle_client(client_socket)

if __name__ == '__main__':
    start_server()