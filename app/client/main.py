import sys
from PySide6 import QtWidgets
from lib.ceasar_encryption import CeasarEncryption
import client.window as window

ceasar = CeasarEncryption(5)

def main():
  app = QtWidgets.QApplication(sys.argv)
  client_window = window.ClientWindow()

  client_window.show()
  sys.exit(app.exec())