import telnetlib

def get_mailbox_size(server, user, password):
    tn = telnetlib.Telnet(server, 110)
    tn.read_until(b"+OK")
    tn.write(f"USER {user}\r\n".encode('ascii'))
    tn.read_until(b"+OK")
    tn.write(f"PASS {password}\r\n".encode('ascii'))
    tn.read_until(b"+OK")
    tn.write(b"STAT\r\n")
    response = tn.read_until(b"\r\n").decode('ascii')
    tn.write(b"QUIT\r\n")
    tn.close()

    msg_count, total_size = response.split()[1:]
    return int(total_size)

server = "interia.pl"
user = "pas2017@interia.pl"
password = "P4SInf2017"

mailbox_size = get_mailbox_size(server, user, password)
print(f"Łączna liczba bajtów zajmowanych przez wiadomości w skrzynce: {mailbox_size}")
