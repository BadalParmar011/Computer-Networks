import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Port = 9099
server.bind(('', Port))
server.listen(5)
while True:
    c, add = server.accept()
    print("Got connection from", end='')
    print(add)
    text = c.recv(1024)
    print('received ' + str(text))
    print('echoing it back')
    c.sendall(text)
    c.close()  # Close the current connection
