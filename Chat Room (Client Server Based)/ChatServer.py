import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Port = 9999
server.bind(('', Port))
server.listen(5)
while True:
    conn, add = server.accept()
    print(add[0] + " connected")  # print the address of the user, that just connected
    while True:
        inputStream_list = [sys.stdin, conn]
        read_sockets, write_socket, error_socket = select.select(inputStream_list, [], [])
        for socket in read_sockets:
            if socket == conn:
                message = socket.recv(2048)
                print("—> Received Message: " + str(message))
        else:
            message = input()
            conn.sendall(message.encode('utf-8'))
            print("—> Your Message: " + str(message))
        if message == 'bye':
            conn.close()
            inputStream_list.remove(conn)
            break
    if conn not in inputStream_list:
        break
    conn.close()  # close the current client
server.close()  # close the server
