import socket
import time

BUFFER_SIZE = 1024
HOST = '127.0.0.1'
TCP_PORT = 12345
UDP_PORT = 12346
NUM_PACKETS = 1000
DATA = b'Test' * 256  # 1024 bajty danych

def tcp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, TCP_PORT))
        start_time = time.time()

        for _ in range(NUM_PACKETS):
            client_socket.sendall(DATA)

        end_time = time.time()
        return end_time - start_time

def udp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        start_time = time.time()

        for _ in range(NUM_PACKETS):
            client_socket.sendto(DATA, (HOST, UDP_PORT))

        end_time = time.time()
        return end_time - start_time

if __name__ == "__main__":
    print("Test przesyłu danych TCP...")
    tcp_time = tcp_client()
    print(f"Czas przesyłu danych TCP: {tcp_time:.4f} sekund")

    print("Test przesyłu danych UDP...")
    udp_time = udp_client()
    print(f"Czas przesyłu danych UDP: {udp_time:.4f} sekund")
