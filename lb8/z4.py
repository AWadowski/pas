import imaplib
import email

def imap_login_and_check_unread_messages(server, port, user, password):
    mail = imaplib.IMAP4(server, port)
    mail.login(user, password)

    mail.select("INBOX")
    status, data = mail.search(None, "UNSEEN")
    unread_msg_nums = data[0].split()

    if len(unread_msg_nums) > 0:
        print(f"Liczba nieprzeczytanych wiadomości: {len(unread_msg_nums)}")
        for num in unread_msg_nums:
            status, data = mail.fetch(num, "(BODY[TEXT])")
            msg_content = data[0][1].decode()
            print(f"Wiadomość {num}:")
            print(msg_content)
            mail.store(num, "+FLAGS", "\\Seen")
            print(f"Wiadomość {num} oznaczona jako przeczytana.")
    else:
        print("Brak nieprzeczytanych wiadomości.")

    mail.logout()

server = "212.182.24.27"
port = 143
user = "pasinf2017@infumcs.edu"
password = "P4SInf2017"

imap_login_and_check_unread_messages(server, port, user, password)
