from threading import Thread
import codecs
import sys
from PySide6 import QtWidgets
from lib.ceasar_encryption import CeasarEncryption
from lib.diff_manchester_code import diff_manchester_decode, string_to_byte
import server.window as window
import server.server as server

ceasar = CeasarEncryption(5)

def parse_msg(msg):
  bin_msg_diff_manchester = ''
  for c in msg:
    bin_msg_diff_manchester += '{0:08b}'.format(c)
  
  bin_msg = diff_manchester_decode(bin_msg_diff_manchester)

  decoded_msg = string_to_byte(bin_msg)
  encrypted_msg = codecs.decode(decoded_msg, 'utf-8')

  msg = ceasar.decrypt(encrypted_msg)
  msg = codecs.decode(msg, "utf-8")

  return {
    "encrypted_msg": encrypted_msg,
    "bin_msg": bin_msg,
    "bin_msg_diff_manchester": bin_msg_diff_manchester,
    "msg": msg,
  }

def main():
  app = QtWidgets.QApplication(sys.argv)

  server_window = window.ServerWindow()
  def handle_msg(msg):
    server_window.on_msg(parse_msg(msg))

  thread = Thread(target=server.tcp_server, args=(handle_msg,))
  thread.setDaemon(True)
  thread.start()

  server_window.show()
  sys.exit(app.exec())