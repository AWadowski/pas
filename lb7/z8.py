import telnetlib

def get_mailbox_messages_size(server, user, password):
    tn = telnetlib.Telnet(server, 110)
    tn.read_until(b"+OK")
    tn.write(f"USER {user}\r\n".encode('ascii'))
    tn.read_until(b"+OK")
    tn.write(f"PASS {password}\r\n".encode('ascii'))
    tn.read_until(b"+OK")
    tn.write(b"STAT\r\n")
    response = tn.read_until(b"\r\n").decode('ascii')
    msg_count = int(response.split()[1])

    message_sizes = []
    for i in range(1, msg_count + 1):
        tn.write(f"LIST {i}\r\n".encode('ascii'))
        response = tn.read_until(b"\r\n").decode('ascii')
        size = int(response.split()[2])
        message_sizes.append(size)

    tn.write(b"QUIT\r\n")
    tn.close()

    return message_sizes

server = "interia.pl"
user = "pas2017@interia.pl"
password = "P4SInf2017"

message_sizes = get_mailbox_messages_size(server, user, password)

for i, size in enumerate(message_sizes, start=1):
    print(f"Wiadomość {i}: {size} bajtów")
