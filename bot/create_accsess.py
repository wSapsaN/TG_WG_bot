import socket
from config import IP_SERVER, PORT

def add_access():

  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  client.connect((IP_SERVER, PORT))
  client.sendall(b"create")

  data = client.recv(1024).decode()

  client.close()

  return data