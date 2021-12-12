import socket

s = socket.socket()
host = socket.gethostname()  # Get local machine name
port = 9999
s.connect((host, port))
with open('received_file.txt', 'wb') as f:
    print("File Opened")
    while True:
        print("receiving data...")
        data = s.recv(100)
        if not data:
            break
        f.write(data)
f.close()
print("Successfully got the file")
print(repr(s.recv(1024)))
s.close()
print("Connection Closed")
