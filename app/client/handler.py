import codecs

from lib.env import get_env
from lib.ceasar_encryption import CeasarEncryption
import lib.diff_manchester_code as diff_manchester_code
import client.client as client

env = get_env()
ceasar = CeasarEncryption(env.get("KEY"))

def get_encrypted_msg(msg):
  encrypted = ceasar.encrypt(msg)
  return codecs.decode(encrypted, "utf-8")

def get_binary_msg(data):
  binary_msg = ''
  for byte in data:
    binary_msg += '{0:08b}'.format(ord(byte))
  return binary_msg

def send_msg(msg):
  msg = diff_manchester_code.bitstring_to_bytes(msg)
  client.send_msg(msg)

def diff_manchester_encode(msg):
  return diff_manchester_code.diff_manchester_encode(msg)
