import telnetlib

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
    tn.write(f"LIST {msg_num}\n".encode('ascii'))
    response = tn.read_until(b"\r\n")
    status, size = response.decode('ascii').strip().split()
    sizes.append(int(size))

for i, size in enumerate(sizes):
    print(f"Wiadomość {i+1} zajmuje {size} bajtów.")

tn.write(b"QUIT\n")
tn.close()