import imaplib

def imap_login_and_delete_message(server, port, user, password, msg_num_to_delete):
    mail = imaplib.IMAP4(server, port)
    mail.login(user, password)

    mail.select("INBOX")
    status, data = mail.search(None, "ALL")
    all_msg_nums = data[0].split()

    if len(all_msg_nums) > 0 and msg_num_to_delete in all_msg_nums:
        mail.store(msg_num_to_delete, "+FLAGS", "\\Deleted")
        mail.expunge()
        print(f"Wiadomość {msg_num_to_delete} została usunięta.")
    else:
        print(f"Nie znaleziono wiadomości o numerze {msg_num_to_delete}.")

    mail.logout()

server = "212.182.24.27"
port = 143
user = "pasinf2017@infumcs.edu"
password = "P4SInf2017"
msg_num_to_delete = b"1"  

imap_login_and_delete_message(server, port, user, password, msg_num_to_delete)
