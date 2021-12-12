import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 3516  # Reserve a port for your service.
s.bind(('', port))  # Bind to the port
s.listen(5)  # Wait for client connection.
while True:
    c, add = s.accept()  # Establish connection
    print('Got connection from', add)
    while True:
        text = c.recv(1024)
        print("received " + str(text) + "\n")
        if text == 'bye':
            break
        msg = input("Enter a msg")
        c.sendall(msg.encode('utf-8'))
        if msg == 'bye':
            break
c.close()  # Close the connection, with current client
