import socket

HOST = '212.182.24.27'
PORT = 2912

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        while True:
            user_number = input('Podaj liczbę do odgadnięcia: ')
            client_socket.sendall(user_number.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            print('Odpowiedź serwera:', response)
            if response == 'Gratulacje! Odgadłeś liczbę!':
                break

if __name__ == '__main__':
    main()