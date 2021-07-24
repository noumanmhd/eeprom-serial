from custom_functions import good_chars
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets

from get_data import SerialData
from custom_functions import good_chars

GOOD_CHARS = good_chars()


class Page(QtWidgets.QWidget):
    def __init__(self, start_addr=0, text_addr=0, text_len=9, port=None):
        super(Page, self).__init__()
        uic.loadUi('new_page.ui', self)
        self.port = port
        self.start_addr = start_addr
        self.text_addr = text_addr
        self.text_len = text_len
        self.write_btn.clicked.connect(self.write_eeprom)
        self.update_btn.clicked.connect(self.read_eeprom)
        

    def write_text(self, ser,  addr, size, text):
        text = [i for i in text if i in GOOD_CHARS]
        if len(text) < size:
            text += [' '] * (size - len(text))  # Add Padding to text
        for i in range(size):
            ser.update(addr + i, ord(text[i]))

    def read_text(self, ser,  addr, size):
        text = []
        for i in range(size):
            c = ser.get(addr + i)
            text.append(chr(c))
        text = [i for i in text if i in GOOD_CHARS]
        if len(text) < size:
            text += [' '] * (size - len(text))
        return ''.join(text)

    def write_eeprom(self):
        if self.port != None:
            self.write_btn.setEnabled(True)
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
                ser.update_ref(9,  self.start_addr,
                               self.spinBox_PC1_10.value())

                ser.update_ref(10,  self.start_addr,
                               self.spinBox_CC1_1.value())
                ser.update_ref(11,  self.start_addr,
                               self.spinBox_CC1_2.value())
                ser.update_ref(12,  self.start_addr,
                               self.spinBox_CC1_3.value())
                ser.update_ref(13,  self.start_addr,
                               self.spinBox_CC1_4.value())
                ser.update_ref(14,  self.start_addr,
                               self.spinBox_CC1_5.value())
                ser.update_ref(15,  self.start_addr,
                               self.spinBox_CC1_6.value())
                ser.update_ref(16,  self.start_addr,
                               self.spinBox_CC1_7.value())
                ser.update_ref(17,  self.start_addr,
                               self.spinBox_CC1_8.value())
                ser.update_ref(18,  self.start_addr,
                               self.spinBox_CC1_9.value())
                ser.update_ref(19,  self.start_addr,
                               self.spinBox_CC1_10.value())

                ser.update_ref(20,  self.start_addr,
                               self.spinBox_CC2_1.value())
                ser.update_ref(21,  self.start_addr,
                               self.spinBox_CC2_2.value())
                ser.update_ref(22,  self.start_addr,
                               self.spinBox_CC2_3.value())
                ser.update_ref(23,  self.start_addr,
                               self.spinBox_CC2_4.value())
                ser.update_ref(24,  self.start_addr,
                               self.spinBox_CC2_5.value())
                ser.update_ref(25,  self.start_addr,
                               self.spinBox_CC2_6.value())
                ser.update_ref(26,  self.start_addr,
                               self.spinBox_CC2_7.value())
                ser.update_ref(27,  self.start_addr,
                               self.spinBox_CC2_8.value())
                ser.update_ref(28,  self.start_addr,
                               self.spinBox_CC2_9.value())
                ser.update_ref(29,  self.start_addr,
                               self.spinBox_CC2_10.value())

                ser.update_ref(30,  self.start_addr,
                               self.spinBox_CC3_1.value())
                ser.update_ref(31,  self.start_addr,
                               self.spinBox_CC3_2.value())
                ser.update_ref(32,  self.start_addr,
                               self.spinBox_CC3_3.value())
                ser.update_ref(33,  self.start_addr,
                               self.spinBox_CC3_4.value())
                ser.update_ref(34,  self.start_addr,
                               self.spinBox_CC3_5.value())
                ser.update_ref(35,  self.start_addr,
                               self.spinBox_CC3_6.value())
                ser.update_ref(36,  self.start_addr,
                               self.spinBox_CC3_7.value())
                ser.update_ref(37,  self.start_addr,
                               self.spinBox_CC3_8.value())
                ser.update_ref(38,  self.start_addr,
                               self.spinBox_CC3_9.value())
                ser.update_ref(39,  self.start_addr,
                               self.spinBox_CC3_10.value())
                self.write_text(ser, self.text_addr, self.text_len, self.bank_name.text())
                ser.close()

            except Exception as e:
                print(e)
        self.write_btn.clearFocus()

    def read_eeprom(self):
        if self.port != None:
            self.update_btn.setEnabled(True)
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

                bank = self.read_text(ser, self.text_addr, self.text_len)
                if bank == ' ' * self.text_len:
                    self.bank_name.setText("*" * self.text_len)
                else:
                    self.bank_name.setText(bank.strip())
                ser.close()

            except Exception as e:
                print(e)
        self.update_btn.clearFocus()

    def set_port(self, port):
        self.port = port
