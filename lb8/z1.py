import telnetlib

def imap_login_and_check_messages(server, port, user, password):
    tn = telnetlib.Telnet(server, port)
    tn.read_until(b"* OK")
    tn.write(b"1 LOGIN " + user.encode("ascii") + b" " + password.encode("ascii") + b"\r\n")
    tn.read_until(b"1 OK")

    tn.write(b"2 LIST \"\" \"*\"\r\n")
    folders = tn.read_until(b"2 OK").decode("ascii")
    print("Skrzynki:")
    print(folders)

    tn.write(b"3 SELECT INBOX\r\n")
    inbox_info = tn.read_until(b"3 OK").decode("ascii")
    print("INBOX:")
    print(inbox_info)

    tn.write(b"4 FETCH 1 BODY[HEADER]\r\n")
    first_msg_header = tn.read_until(b"4 OK").decode("ascii")
    print("Pierwsza dostępna wiadomość:")
    print(first_msg_header)

    tn.write(b"5 STORE 1 +FLAGS \\Seen\r\n")
    tn.read_until(b"5 OK")
    print("Wiadomość oznaczona jako przeczytana.")

    tn.write(b"6 LOGOUT\r\n")
    tn.read_until(b"* BYE")
    tn.close()

server = "212.182.24.27"
port = 143
user = "pasinf2017@infumcs.edu"
password = "P4SInf2017"

imap_login_and_check_messages(server, port, user, password)
