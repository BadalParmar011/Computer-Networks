import socket
from threading import *
serversocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host="localhost"
port=8000
serversocket.bind((host, port))
class client(Thread):
  def __init__(self, socket, address):
    Thread.__init__(self)
    self.sock=socket
    self.addr=address
    self.start()
  def run(self):
    while(True):
      r=input("** Enter data to send: ")
      clientsocket.send(r.encode())
      print(clientsocket.recv(1024).decode())
serversocket.listen(5)
print("** Sender is ready and responding...")
while(True):
  clientsocket, address=serversocket.accept()
  print("Receiver " + str(address) + " connected")
  client(clientsocket, address)
serversocket.close()
