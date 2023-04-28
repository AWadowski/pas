import socket
import threading

class POP3Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)

        print(f"POP3 serwer uruchomiony na {self.host}:{self.port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Połączenie z klientem: {client_address}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        client_socket.sendall(b"+OK Welcome to the POP3 server\r\n")
        authenticated = False

        while True:
            command = client_socket.recv(1024).decode().strip()

            if command == "QUIT":
                client_socket.sendall(b"+OK Goodbye\r\n")
                client_socket.close()
                break

            if not authenticated:
                if command.startswith("USER"):
                    client_socket.sendall(b"+OK Please provide password\r\n")
                elif command.startswith("PASS"):
                    authenticated = True
                    client_socket.sendall(b"+OK Authentication successful\r\n")
                else:
                    client_socket.sendall(b"-ERR Unrecognized command\r\n")
            else:
                if command == "STAT":
                    client_socket.sendall(b"+OK 0 0\r\n")
                elif command == "LIST":
                    client_socket.sendall(b"+OK 0 messages\r\n.\r\n")
                elif command.startswith("RETR"):
                    client_socket.sendall(b"-ERR No messages\r\n")
                else:
                    client_socket.sendall(b"-ERR Unrecognized command\r\n")


pop3_server = POP3Server("127.0.0.1", 1100)
pop3_server.start()
