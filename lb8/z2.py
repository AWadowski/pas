import imaplib

def imap_login_and_check_inbox(server, port, user, password):
    mail = imaplib.IMAP4(server, port)
    mail.login(user, password)

    status, data = mail.select("INBOX")
    if status == "OK":
        msg_count = int(data[0])
        print(f"Liczba wiadomości w skrzynce INBOX: {msg_count}")
    else:
        print("Nie udało się otworzyć skrzynki INBOX")

    mail.logout()

server = "212.182.24.27"
port = 143
user = "pasinf2017@infumcs.edu"
password = "P4SInf2017"

imap_login_and_check_inbox(server, port, user, password)
