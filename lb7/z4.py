import telnetlib
from email.parser import BytesParser
from email.policy import default


tn = telnetlib.Telnet('interia.pl', 110)
tn.read_until(b"User: ")
tn.write('pas2017@interia.pl'.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write('P4SInf2017'.encode('ascii') + b"\n")
tn.write(b"STAT\n")
response = tn.read_until(b"\r\n")
msg_list = response.strip().split('\r\n')[1:-1]
sizes = []
for msg in msg_list:
    msg_num, msg_size = msg.split()
    sizes.append(int(msg_size))
max_size = max(sizes)
max_size_index = sizes.index(max_size) + 1
tn.write(f"RETR {max_size_index}\n".encode('ascii'))
response = tn.read_until(b".\r\n")
msg_data = response.decode('utf-8', errors='replace')
msg = BytesParser(policy=default).parsestr(msg_data)

print(msg.get_body(preferencelist=('plain')).get_content())

tn.write(b"QUIT\n")
tn.close()