import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 9099
s.connect((host, port))
while True:
    data = s.recv(1024).decode()
    print("** Received Data: " + data)
    str = "Acknowledgement: Message Received (" + data + ")"
    s.send(str.encode())
s.close()
