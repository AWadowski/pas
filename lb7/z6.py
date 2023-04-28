import telnetlib


tn = telnetlib.Telnet('interia.pl', 110)
tn.read_until(b"User: ")
tn.write('pas2017@interia.pl'.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write('P4SInf2017'.encode('ascii') + b"\n")
tn.write(b"STAT\n")
tn.write(b"STAT\n")
response = tn.read_until(b"\r\n").decode('ascii')
msg_count = response.split()[1]

print(f"Liczba wiadomości w skrzynce: {msg_count}")

tn.write(b"QUIT\n")
tn.close()