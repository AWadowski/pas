import socket

HOST = '127.0.0.1'
PORT = 9214
BUFFER_SIZE = 1024

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server listening on {HOST}:{PORT}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                conn.sendall(data)

if __name__ == '__main__':
    start_server()