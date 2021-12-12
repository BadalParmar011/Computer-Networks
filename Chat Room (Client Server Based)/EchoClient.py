import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9099
s.connect(("127.0.0.1", port))
text = input("Enter a message to send: ")
s.sendall(text.encode('utf-8'))
print(s.recv(1024))
