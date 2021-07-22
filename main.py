import os
import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

# Local functions and classes
from get_data import SerialData
from custom_functions import get_ports


class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        layout = QtWidgets.QVBoxLayout()
        
        ports_layout = QtWidgets.QHBoxLayout()
        self.p_list = QtWidgets.QComboBox()
        self.set_ports()
        self.p_list.currentIndexChanged.connect(self.selection_change)
        ports_layout.addWidget(self.p_list)

        detect_btn = QtWidgets.QPushButton('Detect Ports', self)
        detect_btn.setToolTip('Click to detect ports')
        detect_btn.clicked.connect(self.set_ports)
        ports_layout.addWidget(detect_btn)

        layout.addLayout(ports_layout)
        self.setLayout(layout)

    def set_ports(self):
        self.ports = get_ports()
        self.p_list.clear()
        if len(self.ports) > 0:
            self.p_list.addItem('--- Select Port ---')
            for port in self.ports:
                self.p_list.addItem(f'{port["product"]} ({port["device"]})')
        else:
            self.p_list.addItem("--- No device detected ---")

    def selection_change(self, value):
        if value > 0:
            port = self.ports[value - 1]["device"]
            print(port)
    



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    # window.setWindowState(QtCore.Qt.WindowMaximized)
    window.setFixedSize(1104,614)
    qtRectangle = window.frameGeometry()
    centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
    qtRectangle.moveCenter(centerPoint)
    window.move(qtRectangle.topLeft())
    # window.setWindowIcon(QtGui.QIcon('images/icon.png'))
    widget = MainWidget()
    window.setWindowTitle("EEPROM")
    window.setCentralWidget(widget)
    window.show()
    sys.exit(app.exec_())