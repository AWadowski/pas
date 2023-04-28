import telnetlib

def get_largest_message(server, user, password):
    tn = telnetlib.Telnet(server, 110)
    tn.read_until(b"+OK")
    tn.write(f"USER {user}\r\n".encode('ascii'))
    tn.read_until(b"+OK")
    tn.write(f"PASS {password}\r\n".encode('ascii'))
    tn.read_until(b"+OK")
    tn.write(b"STAT\r\n")
    response = tn.read_until(b"\r\n").decode('ascii')
    msg_count = int(response.split()[1])

    largest_msg_index = 0
    largest_msg_size = 0

    for i in range(1, msg_count + 1):
        tn.write(f"LIST {i}\r\n".encode('ascii'))
        response = tn.read_until(b"\r\n").decode('ascii')
        size = int(response.split()[2])
        if size > largest_msg_size:
            largest_msg_size = size
            largest_msg_index = i

    tn.write(f"RETR {largest_msg_index}\r\n".encode('ascii'))
    largest_msg_content = tn.read_until(b"\r\n.\r\n").decode('ascii')

    tn.write(b"QUIT\r\n")
    tn.close()

    return largest_msg_content

server = "interia.pl"
user = "pas2017@interia.pl"
password = "P4SInf2017"

largest_message = get_largest_message(server, user, password)
print("Treść wiadomości o największym rozmiarze:")
print(largest_message)
