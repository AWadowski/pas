import telnetlib

tn = telnetlib.Telnet('interia.pl', 110)
tn.read_until(b"User: ")
tn.write('pas2017@interia.pl'.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write('P4SInf2017'.encode('ascii') + b"\n")
tn.write(b"STAT\n")
response = tn.read_until(b"\r\n")
status, num_msgs, total_bytes = response.decode('ascii').strip().split()
total_bytes = int(total_bytes)
print(f"Wszystkie wiadomości zajmują {total_bytes} bajtów.")
tn.write(b"QUIT\n")
tn.close()