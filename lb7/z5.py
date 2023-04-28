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
min_size = min(sizes)
min_size_index = sizes.index(min_size) + 1
tn.write(f"DELE {min_size_index}\n".encode('ascii'))
response = tn.read_until(b"\r\n").decode('ascii')

tn.write(b"QUIT\n")
tn.close()