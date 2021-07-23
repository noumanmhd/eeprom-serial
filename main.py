import os
import sys

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets


# Local functions and classes
from page import Page
from first_page import FirstPage
from custom_functions import get_ports

NUMBER_OF_PAGES = 5

# Number of memory addresses for each page
PAGE_MEMORY = 75


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

        self.tabs = QtWidgets.QTabWidget()
        self.add_pages()
        layout.addWidget(self.tabs)

        file_layout = QtWidgets.QHBoxLayout()
        save_btn = QtWidgets.QPushButton('Save all preset to file', self)
        # save_btn.clicked.connect(self.set_ports)
        
        load_btn = QtWidgets.QPushButton('Load presets from file', self)
        # load_btn.clicked.connect(self.set_ports)
        
        file_layout.addWidget(load_btn)
        file_layout.addWidget(save_btn)

        layout.addLayout(file_layout)
        self.setLayout(layout)

    def add_pages(self):
        """ Function to add Pages and create there tabs """
        self.pages = []
        self.pages.append(FirstPage(start_addr=0))
        self.tabs.addTab(self.pages[0], f'Page 1')
        for i in range(1, NUMBER_OF_PAGES):
            self.pages.append(Page(start_addr=(i*PAGE_MEMORY)))
            self.tabs.addTab(self.pages[i], f'Page {i+1}')

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
            for page in self.pages:
                page.set_port(port)
                page.read_eeprom()
                self.p_list.clearFocus()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    # window.setWindowState(QtCore.Qt.WindowMaximized)
    window.setFixedSize(1220, 710)
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
