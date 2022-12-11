from PySide6 import QtCore, QtWidgets

from matplotlib.backends.backend_qtagg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import client.handler as handler

class ClientWindow(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()

    self.msg = QtWidgets.QLineEdit()
    self.msg.textChanged.connect(self.on_msg_changed)
    
    self.encrypted_msg = QtWidgets.QTableWidgetItem()
    self.bin_msg = QtWidgets.QTableWidgetItem()
    self.bin_msg_diff_manchester = QtWidgets.QTableWidgetItem()

    self.send_button = QtWidgets.QPushButton('Send')
    self.send_button.clicked.connect(self.send_msg)

    self.canvas = self.build_canvas()
    form_layout = QtWidgets.QFormLayout()
    form_layout.addRow('Message:', self.msg)
    
    table = QtWidgets.QTableWidget(3,1)
    table.setVerticalHeaderLabels(["Encrypted Message", "Binary Message", "Differential Manchester Encoded Message"])
    table.setHorizontalHeaderLabels(["Data"])
    table.horizontalHeader().setDefaultSectionSize(620)
    table.verticalHeader().setDefaultSectionSize(40)
    table.setItem(0, 0, self.encrypted_msg)
    table.setItem(1, 0, self.bin_msg)
    table.setItem(2, 0, self.bin_msg_diff_manchester)
    form_layout.addWidget(table)

    form_layout.addRow(self.canvas)
    form_layout.addRow(self.send_button)

    self.setLayout(form_layout)
    self.setWindowTitle('Client')

  def build_canvas(self):
    canvas = FigureCanvas(Figure(figsize=(8, 3)))
    self.canvas_subplots = canvas.figure.subplots()
    return canvas

  def update_canvas(self):
    self.canvas_subplots.cla()
    data = self.bin_msg_diff_manchester.text()
    if len(data) > 0:
      y = [int(c) for c in data]
      y.append(y[-1])

      x = [v / 2 for v in range(len(y))]
      self.canvas_subplots.step(x, y, where='post')

    self.canvas_subplots.figure.canvas.draw()

  @QtCore.Slot(str)
  def on_msg_changed(self, msg):
    encrypted = handler.get_encrypted_msg(msg)
    self.encrypted_msg.setText(encrypted)
    self.bin_msg.setText(handler.get_bin_msg(encrypted))
    self.bin_msg_diff_manchester.setText(handler.diff_manchester_encode(encrypted))
    self.update_canvas()

  @QtCore.Slot()
  def send_msg(self):
    handler.send_msg(self.bin_msg_diff_manchester.text())
