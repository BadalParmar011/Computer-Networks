# This program will chat only one message at a time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 3516  # Reserve a port for your service
s.connect(("127.0.0.1", port))
while True:
    text = input("Enter a message to send: ")
    s.sendall(text.encode('utf-8'))
    if text == 'bye':
        break
    msg = s.recv(1024)
    print('received ' + str(msg))
    if msg == 'bye':
        break
