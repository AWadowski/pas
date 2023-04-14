import smtplib
from email.message import EmailMessage

login = "pas2017@interia.pl"
password = "P4SInf2017"

msg = EmailMessage()
msg.set_content("Treść wiadomości")

receivers = " , ".join["adam.wadowskik@gmail.com", "adamwadowski@gmail.com"]
msg["Subject"] = "Temat wiadomości"
msg["From"] = login
msg["To"] = receivers
with smtplib.SMTP("poczta.interia.pl", 587) as server:
    server.starttls()
    server.login(login, password)
    server.send_message(msg)

print("Wiadomość e-mail została wysłana pomyślnie.")
