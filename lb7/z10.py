import telnetlib

def get_all_messages(server, user, password):
    tn = telnetlib.Telnet(server, 110)
    tn.read_until(b"+OK")
    tn.write(f"USER {user}\r\n".encode('ascii'))
    tn.read_until(b"+OK")
    tn.write(f"PASS {password}\r\n".encode('ascii'))
    tn.read_until(b"+OK")
    tn.write(b"STAT\r\n")
    response = tn.read_until(b"\r\n").decode('ascii')
    msg_count = int(response.split()[1])

    messages = []

    for i in range(1, msg_count + 1):
        tn.write(f"RETR {i}\r\n".encode('ascii'))
        msg_content = tn.read_until(b"\r\n.\r\n").decode('ascii')
        messages.append(msg_content)

    tn.write(b"QUIT\r\n")
    tn.close()

    return messages

server = "interia.pl"
user = "pas2017@interia.pl"
password = "P4SInf2017"

all_messages = get_all_messages(server, user, password)

for i, message in enumerate(all_messages, start=1):
    print(f"Wiadomość {i}:")
    print(message)
    print("---------------------------------------------------")
