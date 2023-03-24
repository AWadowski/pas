import socket

HOST = '127.0.0.1'
PORT = 5000

def parse_message(message):
    parts = message.split(';')
    if len(parts) != 7:
        return None
    try:
        ver = int(parts[1])
        srcip = parts[3]
        dstip = parts[5]
        type = int(parts[7])
        srcport = int(parts[9])
        dstport = int(parts[11])
        data = parts[13]
    except ValueError:
        return None
    return (ver, srcip, dstip, type, srcport, dstport, data)

def handle_message(sock, addr, message):
    parsed = parse_message(message)
    if parsed is None:
        response = 'BADSYNTAX'
    else:
        response = 'TAK'
    sock.sendto(response.encode('utf-8'), addr)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((HOST, PORT))
        print(f'Starting UDP server on {HOST}:{PORT}...')
        while True:
            data, addr = sock.recvfrom(1024)
            message = data.decode('utf-8')
            handle_message(sock, addr, message)

if __name__ == '__main__':
    main()
