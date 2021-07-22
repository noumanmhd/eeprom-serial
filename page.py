from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets

from get_data import SerialData

class Page(QtWidgets.QWidget):
    def __init__(self, start_addr=0, port=None):
        super(Page, self).__init__()
        uic.loadUi('page.ui', self)
        self.port = port
        self.start_addr = start_addr
        self.write_btn.clicked.connect(self.write_eeprom)
        self.update_btn.clicked.connect(self.read_eeprom)

    def write_eeprom(self):
        if self.port != None:
            try:
                ser = SerialData(port=self.port)

                ser.update_ref(0,  self.start_addr, self.spinBox_PC1_1.value())
                ser.update_ref(1,  self.start_addr, self.spinBox_PC1_2.value())
                ser.update_ref(2,  self.start_addr, self.spinBox_PC1_3.value())
                ser.update_ref(3,  self.start_addr, self.spinBox_PC1_4.value())
                ser.update_ref(4,  self.start_addr, self.spinBox_PC1_5.value())
                ser.update_ref(5,  self.start_addr, self.spinBox_PC1_6.value())
                ser.update_ref(6,  self.start_addr, self.spinBox_PC1_7.value())
                ser.update_ref(7,  self.start_addr, self.spinBox_PC1_8.value())
                ser.update_ref(8,  self.start_addr, self.spinBox_PC1_9.value())
                ser.update_ref(9,  self.start_addr, self.spinBox_PC1_10.value())

                ser.update_ref(10,  self.start_addr, self.spinBox_CC1_1.value())
                ser.update_ref(11,  self.start_addr, self.spinBox_CC1_2.value())
                ser.update_ref(12,  self.start_addr, self.spinBox_CC1_3.value())
                ser.update_ref(13,  self.start_addr, self.spinBox_CC1_4.value())
                ser.update_ref(14,  self.start_addr, self.spinBox_CC1_5.value())
                ser.update_ref(15,  self.start_addr, self.spinBox_CC1_6.value())
                ser.update_ref(16,  self.start_addr, self.spinBox_CC1_7.value())
                ser.update_ref(17,  self.start_addr, self.spinBox_CC1_8.value())
                ser.update_ref(18,  self.start_addr, self.spinBox_CC1_9.value())
                ser.update_ref(19,  self.start_addr, self.spinBox_CC1_10.value())

                ser.update_ref(20,  self.start_addr, self.spinBox_CC2_1.value())
                ser.update_ref(21,  self.start_addr, self.spinBox_CC2_2.value())
                ser.update_ref(22,  self.start_addr, self.spinBox_CC2_3.value())
                ser.update_ref(23,  self.start_addr, self.spinBox_CC2_4.value())
                ser.update_ref(24,  self.start_addr, self.spinBox_CC2_5.value())
                ser.update_ref(25,  self.start_addr, self.spinBox_CC2_6.value())
                ser.update_ref(26,  self.start_addr, self.spinBox_CC2_7.value())
                ser.update_ref(27,  self.start_addr, self.spinBox_CC2_8.value())
                ser.update_ref(28,  self.start_addr, self.spinBox_CC2_9.value())
                ser.update_ref(29,  self.start_addr, self.spinBox_CC2_10.value())

                ser.update_ref(30,  self.start_addr, self.spinBox_CC3_1.value())
                ser.update_ref(31,  self.start_addr, self.spinBox_CC3_2.value())
                ser.update_ref(32,  self.start_addr, self.spinBox_CC3_3.value())
                ser.update_ref(33,  self.start_addr, self.spinBox_CC3_4.value())
                ser.update_ref(34,  self.start_addr, self.spinBox_CC3_5.value())
                ser.update_ref(35,  self.start_addr, self.spinBox_CC3_6.value())
                ser.update_ref(36,  self.start_addr, self.spinBox_CC3_7.value())
                ser.update_ref(37,  self.start_addr, self.spinBox_CC3_8.value())
                ser.update_ref(38,  self.start_addr, self.spinBox_CC3_9.value())
                ser.update_ref(39,  self.start_addr, self.spinBox_CC3_10.value())

                ser.close()
            
            except Exception as e:
                print(e)


    def read_eeprom(self):
        if self.port != None:
            try:
                ser = SerialData(port=self.port)

                self.spinBox_PC1_1.setValue(ser.get_ref(0,  self.start_addr))
                self.spinBox_PC1_2.setValue(ser.get_ref(1,  self.start_addr))
                self.spinBox_PC1_3.setValue(ser.get_ref(2,  self.start_addr))
                self.spinBox_PC1_4.setValue(ser.get_ref(3,  self.start_addr))
                self.spinBox_PC1_5.setValue(ser.get_ref(4,  self.start_addr))
                self.spinBox_PC1_6.setValue(ser.get_ref(5,  self.start_addr))
                self.spinBox_PC1_7.setValue(ser.get_ref(6,  self.start_addr))
                self.spinBox_PC1_8.setValue(ser.get_ref(7,  self.start_addr))
                self.spinBox_PC1_9.setValue(ser.get_ref(8,  self.start_addr))
                self.spinBox_PC1_10.setValue(ser.get_ref(9,  self.start_addr))
                
                self.spinBox_CC1_1.setValue(ser.get_ref(10,  self.start_addr))
                self.spinBox_CC1_2.setValue(ser.get_ref(11,  self.start_addr))
                self.spinBox_CC1_3.setValue(ser.get_ref(12,  self.start_addr))
                self.spinBox_CC1_4.setValue(ser.get_ref(13,  self.start_addr))
                self.spinBox_CC1_5.setValue(ser.get_ref(14,  self.start_addr))
                self.spinBox_CC1_6.setValue(ser.get_ref(15,  self.start_addr))
                self.spinBox_CC1_7.setValue(ser.get_ref(16,  self.start_addr))
                self.spinBox_CC1_8.setValue(ser.get_ref(17,  self.start_addr))
                self.spinBox_CC1_9.setValue(ser.get_ref(18,  self.start_addr))
                self.spinBox_CC1_10.setValue(ser.get_ref(19,  self.start_addr))
                
                self.spinBox_CC2_1.setValue(ser.get_ref(20,  self.start_addr))
                self.spinBox_CC2_2.setValue(ser.get_ref(21,  self.start_addr))
                self.spinBox_CC2_3.setValue(ser.get_ref(22,  self.start_addr))
                self.spinBox_CC2_4.setValue(ser.get_ref(23,  self.start_addr))
                self.spinBox_CC2_5.setValue(ser.get_ref(24,  self.start_addr))
                self.spinBox_CC2_6.setValue(ser.get_ref(25,  self.start_addr))
                self.spinBox_CC2_7.setValue(ser.get_ref(26,  self.start_addr))
                self.spinBox_CC2_8.setValue(ser.get_ref(27,  self.start_addr))
                self.spinBox_CC2_9.setValue(ser.get_ref(28,  self.start_addr))
                self.spinBox_CC2_10.setValue(ser.get_ref(29,  self.start_addr))

                self.spinBox_CC3_1.setValue(ser.get_ref(30,  self.start_addr))
                self.spinBox_CC3_2.setValue(ser.get_ref(31,  self.start_addr))
                self.spinBox_CC3_3.setValue(ser.get_ref(32,  self.start_addr))
                self.spinBox_CC3_4.setValue(ser.get_ref(33,  self.start_addr))
                self.spinBox_CC3_5.setValue(ser.get_ref(34,  self.start_addr))
                self.spinBox_CC3_6.setValue(ser.get_ref(35,  self.start_addr))
                self.spinBox_CC3_7.setValue(ser.get_ref(36,  self.start_addr))
                self.spinBox_CC3_8.setValue(ser.get_ref(37,  self.start_addr))
                self.spinBox_CC3_9.setValue(ser.get_ref(38,  self.start_addr))
                self.spinBox_CC3_10.setValue(ser.get_ref(39,  self.start_addr))

                ser.close()
            
            except Exception as e:
                print(e)

    def set_port(self, port):
        self.port = port
