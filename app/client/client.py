import socket
from lib.ceasar_encryption import CeasarEncryption

def send_msg(msg):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("localhost", 30001))
    s.sendall(msg)