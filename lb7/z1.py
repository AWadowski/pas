import telnetlib

tn = telnetlib.Telnet('interia.pl', 110)
tn.read_until(b"User: ")
tn.write('pas2017@interia.pl'.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write('P4SInf2017'.encode('ascii') + b"\n")
tn.write(b'STAT\r\n')
response = tn.read_until(b'\r\n').decode('ascii').strip()
tn.close()
num_messages = int(response.split()[0])
print('Liczba wiadomości w skrzynce:', num_messages)
