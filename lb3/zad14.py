import socket


datagram = "0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18 00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee 00 1a 4c ee 68 65 6c 6c 6f 20 3a 29".split()
source_port = int("".join(datagram[:2]), 16)
dest_port = int("".join(datagram[2:4]), 16)
data = "".join([chr(int(x, 16)) for x in datagram[8:]])
print(source_port)
print(dest_port)
print(data)
odp = f"zad13odp;src;{source_port};dst;{dest_port};data;{data}"

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
result_stream = client.connect_ex(('212.182.24.236', 2909))

client.settimeout(1)
client.send(odp.encode('utf-8'))
result = client.recv(1024)
print(result.decode())

client.close()