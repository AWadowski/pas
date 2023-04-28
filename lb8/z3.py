import imaplib

def imap_login_and_check_all_folders(server, port, user, password):
    mail = imaplib.IMAP4(server, port)
    mail.login(user, password)

    status, folders = mail.list()
    total_msg_count = 0

    if status == "OK":
        for folder in folders:
            folder_name = folder.decode().split()[-1]
            status, data = mail.select(folder_name, readonly=True)
            if status == "OK":
                msg_count = int(data[0])
                total_msg_count += msg_count
                print(f"Liczba wiadomości w skrzynce {folder_name}: {msg_count}")
            else:
                print(f"Nie udało się otworzyć skrzynki {folder_name}")

        print(f"Łączna liczba wiadomości we wszystkich skrzynkach: {total_msg_count}")

    mail.logout()

server = "212.182.24.27"
port = 143
user = "pasinf2017@infumcs.edu"
password = "P4SInf2017"

imap_login_and_check_all_folders(server, port, user, password)
