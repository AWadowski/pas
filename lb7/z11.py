import telnetlib
import base64
import os
import re
from email.parser import Parser

def save_image_attachment(server, user, password):
    tn = telnetlib.Telnet(server, 110)
    tn.read_until(b"+OK")
    tn.write(f"USER {user}\r\n".encode('ascii'))
    tn.read_until(b"+OK")
    tn.write(f"PASS {password}\r\n".encode('ascii'))
    tn.read_until(b"+OK")
    tn.write(b"STAT\r\n")
    response = tn.read_until(b"\r\n").decode('ascii')
    msg_count = int(response.split()[1])

    for i in range(1, msg_count + 1):
        tn.write(f"RETR {i}\r\n".encode('ascii'))
        msg_content = tn.read_until(b"\r\n.\r\n").decode('ascii')
        msg = Parser().parsestr(msg_content)

        if msg.is_multipart():
            for part in msg.walk():
                content_disposition = part.get("Content-Disposition")
                if content_disposition and "attachment" in content_disposition:
                    file_name = re.findall(r'filename="([^"]+)"', content_disposition)[0]
                    file_data = part.get_payload()

                    if part.get_content_type().startswith("image"):
                        with open(file_name, "wb") as f:
                            f.write(base64.b64decode(file_data))
                        print(f"Obrazek '{file_name}' został zapisany na dysku.")
                        break

    tn.write(b"QUIT\r\n")
    tn.close()

server = "interia.pl"
user = "pas2017@interia.pl"
password = "P4SInf2017"

save_image_attachment(server, user, password)
