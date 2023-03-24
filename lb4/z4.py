import socket

HOST = '127.0.0.1'
PORT = 9000
BUFFER_SIZE = 1024

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((HOST, PORT))
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            data, address = server_socket.recvfrom(BUFFER_SIZE)
            print(f"Received message from {address}: {data.decode('utf-8')}")
            operands = data.decode('utf-8').split()
            if len(operands) != 3:
                server_socket.sendto("Invalid data format".encode('utf-8'), address)
                continue
            try:
                num1 = float(operands[0])
                num2 = float(operands[2])
                operator = operands[1]
                if operator == '+':
                    result = num1 + num2
                elif operator == '-':
                    result = num1 - num2
                elif operator == '*':
                    result = num1 * num2
                elif operator == '/':
                    result = num1 / num2
                else:
                    server_socket.sendto("Invalid operator".encode('utf-8'), address)
                    continue
                server_socket.sendto(str(result).encode('utf-8'), address)
            except ValueError:
                server_socket.sendto("Invalid operand(s)".encode('utf-8'), address)
                continue

if __name__ == '__main__':
    start_server()
