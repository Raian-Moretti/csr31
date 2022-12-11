from PySide6 import QtCore, QtWidgets
from matplotlib.backends.backend_qtagg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

class ServerWindow(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()

    self.msg = QtWidgets.QTableWidgetItem()
    self.encrypted_msg = QtWidgets.QTableWidgetItem()
    self.bin_msg = QtWidgets.QTableWidgetItem()
    self.bin_msg_diff_manchester = QtWidgets.QTableWidgetItem()

    self.canvas = self.build_canvas()
    form_layout = QtWidgets.QFormLayout()

    table = QtWidgets.QTableWidget(4,1)
    table.setVerticalHeaderLabels(["Differential Manchester Encoded Message", "Binary Message", "Encrypted Message", "Message"])
    table.setHorizontalHeaderLabels(["Data"])
    table.horizontalHeader().setDefaultSectionSize(620)
    table.verticalHeader().setDefaultSectionSize(40)
    table.setItem(0, 0, self.bin_msg_diff_manchester)
    table.setItem(1, 0, self.bin_msg)
    table.setItem(2, 0, self.encrypted_msg)
    table.setItem(3, 0, self.msg)
    form_layout.addWidget(table)

    form_layout.addRow(self.canvas)

    self.setLayout(form_layout)
    self.setWindowTitle('Server')

  @QtCore.Slot(dict)
  def on_msg(self, data):
    self.bin_msg_diff_manchester.setText(data['bin_msg_diff_manchester'])
    self.update_canvas()
    self.msg.setText(data['msg'])
    self.encrypted_msg.setText(data['encrypted_msg'])
    self.bin_msg.setText(data['bin_msg'])

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
