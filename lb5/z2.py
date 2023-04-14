import socket
import random

HOST = '127.0.0.1'
PORT = 12345

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Serwer uruchomiony na {HOST}:{PORT}")
        secret_number = random.randint(1, 100)
        print(f"Wylosowana liczba: {secret_number}")

        client_socket, client_address = server_socket.accept()

        with client_socket:
            print(f"Połączono z {client_address}")
            while True:
                try:
                    message = client_socket.recv(1024).decode('utf-8')
                    guessed_number = int(message)

                    if guessed_number < secret_number:
                        response = "Liczba jest mniejsza niż wylosowana."
                    elif guessed_number > secret_number:
                        response = "Liczba jest większa niż wylosowana."
                    else:
                        response = "Gratulacje! Odgadłeś liczbę!"
                        client_socket.sendall(response.encode('utf-8'))
                        break

                    client_socket.sendall(response.encode('utf-8'))

                except ValueError:
                    response = "Błąd: Oczekiwano liczby."
                    client_socket.sendall(response.encode('utf-8'))

if __name__ == '__main__':
    main()
