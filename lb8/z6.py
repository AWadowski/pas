import socket
import threading

def imap_server_client_handler(client_socket):
    client_socket.send(b"* OK IMAP4rev1 Server Ready\r\n")
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        command = data.split(" ")[0].upper()

        if command == "LOGIN":
            client_socket.send(b"OK LOGIN completed\r\n")
        elif command == "SELECT":
            client_socket.send(b"* 2 EXISTS\r\n")
            client_socket.send(b"* 0 RECENT\r\n")
            client_socket.send(b"OK [READ-WRITE] SELECT completed\r\n")
        elif command == "FETCH":
            client_socket.send(b"* 1 FETCH (BODY[TEXT] {12}\r\n")
            client_socket.send(b"Hello world!)\r\n")
            client_socket.send(b"OK FETCH completed\r\n")
        elif command == "LOGOUT":
            client_socket.send(b"* BYE IMAP4rev1 Server logging out\r\n")
            client_socket.send(b"OK LOGOUT completed\r\n")
            break
        else:
            client_socket.send(b"BAD Unrecognized command\r\n")

    client_socket.close()

def imap_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", port))
    server.listen(5)
    print(f"IMAP server is listening on port {port}")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=imap_server_client_handler, args=(client_socket,))
        client_handler.start()

port = 12345
imap_server(port)
