import codecs
from lib.ceasar_encryption import CeasarEncryption
import lib.diff_manchester_code as diff_manchester_code
import client.client as client
ceasar = CeasarEncryption(5)

def get_encrypted_msg(msg):
  encrypted = ceasar.encrypt(msg)
  return codecs.decode(encrypted, "utf-8")

def get_bin_msg(data):
  bin_msg = ''
  for byte in data:
    bin_msg += '{0:08b}'.format(ord(byte))
  return bin_msg

def send_msg(msg):
  msg = diff_manchester_code.string_to_byte(msg)
  client.send_msg(msg)

def diff_manchester_encode(msg):
  return diff_manchester_code.diff_manchester_encode(msg)
