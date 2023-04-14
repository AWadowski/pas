import socket
from itertools import permutations

HOST = '212.182.24.27'
UDP_PORT = 666
TCP_PORT = 2913
MAX_PORT_RANGE = 65535

def send_udp_packet(sock, port):
    sock.sendto(b"PING", (HOST, port))
    response, _ = sock.recvfrom(1024)
    return response.decode() == "PONG"

def main():
    print("Szukanie sekwencji")
    sequence = []
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        udp_socket.settimeout(1)
        for port in range(UDP_PORT, MAX_PORT_RANGE, 666):
            if send_udp_packet(udp_socket, port):
                sequence.append(port)
                if len(sequence) == 3:
                    break
    
    print(f"Znaleziono sekwencję: {sequence}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
        for port in sequence:
            tcp_socket.connect((HOST, port))
            tcp_socket.close()
            tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        tcp_socket.connect((HOST, TCP_PORT))
        response = tcp_socket.recv(1024).decode()
        print(response)
if __name__ == '__main__':
    main()
