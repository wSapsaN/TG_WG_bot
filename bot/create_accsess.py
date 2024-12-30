import socket
import os
from config import IP_SERVER, PORT

def __add_access(name_us: str, ip_addr: str):
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  msg = f"/home/uniq/main_test.sh {name_us} {ip_addr}"

  client.connect((IP_SERVER, PORT))
  client.sendall(bytes(msg, "utf-8"))

  data = client.recv(1024).decode()
  
  client.close()

  return data

def create_accsess(name_us: str, ip_addr: str):
  private_key = __add_access(name_us=name_us, ip_addr=ip_addr)

  os.system(f"./bot/bot_createUS.sh {name_us} {private_key} {ip_addr}")

  return f"{name_us}.conf"

# Example: 
#   create_accsess("test", "10.10.10.2")