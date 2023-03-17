import socket


datagram = "ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f 6e 20 69 73 20 66 75 6e".split()
source_port = int("".join(datagram[:2]), 16)
dest_port = int("".join(datagram[2:4]), 16)
data = "".join([chr(int(x, 16)) for x in datagram[8:]])
print(source_port)
print(dest_port)
print(data)
odp = f"zad14odp;src;{source_port};dst;{dest_port};data;{data}"
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
result_stream = client.connect_ex(('212.182.24.236', 2910))
client.settimeout(1)
client.send(odp.encode('utf-8'))
result = client.recv(1024)
print(result.decode())

client.close()