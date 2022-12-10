import sys

from PySide6 import QtWidgets

from lib.env import get_env
from lib.ceasar_encryption import CeasarEncryption
import client.window as window

env = get_env()
ceasar = CeasarEncryption(env.get("KEY"))

def main():
  app = QtWidgets.QApplication(sys.argv)
  client_window = window.ClientWindow()

  client_window.show()
  sys.exit(app.exec_())