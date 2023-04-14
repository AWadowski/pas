import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

login = "pas2017@interia.pl"
password = "P4SInf2017"

msg = MIMEMultipart()
msg["Subject"] = "Temat wiadomości"
msg["From"] = login
msg["To"] = "adam.wadowskik@gmail.com"

msg.attach(MIMEText("Treść wiadomości", "plain"))

filename = "text.txt"
with open(filename, "rb") as attachment:
    encoded = base64.b64encode(attachment.read())
    payload = MIMEBase("application", "octet-stream")
    payload.set_payload(encoded)
    encoders.encode_base64(payload)
    payload.add_header("Content-Disposition", f"attachment; filename={filename}")
    msg.attach(payload)

with smtplib.SMTP("poczta.interia.pl", 587) as server:
    server.starttls()
    server.login(login, password)
    server.send_message(msg)

print("Wiadomość e-mail została wysłana pomyślnie.")
