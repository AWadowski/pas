import socket
import time

BUFFER_SIZE = 1024
HOST = '127.0.0.1'
TCP_PORT = 12345
UDP_PORT = 12346

def tcp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, TCP_PORT))
        server_socket.listen(1)
        conn, _ = server_socket.accept()
        with conn:
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break

def udp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((HOST, UDP_PORT))
        while True:
            data, _ = server_socket.recvfrom(BUFFER_SIZE)
            if not data:
                break

if __name__ == "__main__":
    print("Serwer TCP uruchomiony...")
    tcp_server()
    time.sleep(5)
    print("Serwer UDP uruchomiony...")
    udp_server()
