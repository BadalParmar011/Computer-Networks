import socket
port=60000
s=socket.socket()
host=socket.gethostname() #Get local machine name
s.bind((host, port)) #Bind to the port
s.listen(5) #Wait for client connection.
print("Server listening....")
while(True):
    conn, add=s.accept()
    print("Got connection from", add)
    filename='mytext.txt'
    f=open(filename,'rb')
    l=f.read(100)
    while(l):
      conn.send(l)
      print("Sent ", repr(l))
      l=f.read(100)
    f.close()
    print('Done Sending')
    conn.close() #Close the current connection
