import socket
import select
import sys

import socks

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(s)
IP_address = '127.0.0.1'
Port = 12348
s.connect((IP_address, Port))
while True:
    inputStream_list = [sys.stdin, s]
    read_sockets, write_socket, error_socket = select.select(inputStream_list, [], [])
    for socket in read_sockets:
        if socket == s:
            message = socks.recv(2048)
            print("—> Received Message: " + str(message))
        else:
            message = input()
            s.sendall(message.encode('utf-8'))
            print("—> Your Message: " + str(message))
            if message == 'bye':
                s.close()
                inputStream_list.remove(s)
                break
    if s not in inputStream_list:
        break
s.close()  # close the socket
