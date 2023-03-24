import socket

datagram = "45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1 80 18 00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 01 00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 73 20 66 75 6e".split()

first_byte = bin(int(datagram[0], 16))[2:-4]
ver = int(first_byte, 2)
srcip = ".".join([str(int(x, 16)) for x in datagram[12:16]])
dstip = ".".join([str(int(x, 16)) for x in datagram[16:20]])
type = 6
srcport = int("".join(datagram[20:22]), 16)
dstport = int("".join(datagram[22:24]), 16)
data = "".join([chr(int(x, 16)) for x in datagram[52:]])


odp1 = f"zad15odpA;ver;{ver};srcip;{srcip};dstip;{dstip};type;{type}"
odp2 = f"zad15odpB;srcport;{srcport};dstport;{dstport};data;{data}"

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
result_stream = client.connect_ex(('212.182.24.236', 2911))

client.settimeout(1)
client.send(odp1.encode('utf-8'))
result = client.recv(1024)
client.send(odp2.encode('utf-8'))
print(result.decode())

client.close()