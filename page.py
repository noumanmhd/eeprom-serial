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

    def set_dropdown(self, obj, size, value):
        if value < size:
            obj.setCurrentIndex(value)
        else:
            obj.setCurrentIndex(0)

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

                ser.update_ref(40, self.start_addr,
                               self.presetLabel1_1.currentIndex())
                ser.update_ref(41, self.start_addr,
                               self.presetLabel1_2.currentIndex())
                ser.update_ref(42, self.start_addr,
                               self.presetLabel1_3.currentIndex())
                ser.update_ref(43, self.start_addr,
                               self.presetLabel1_4.currentIndex())
                ser.update_ref(44, self.start_addr,
                               self.presetLabel1_5.currentIndex())
                ser.update_ref(45, self.start_addr,
                               self.presetLabel1_6.currentIndex())
                ser.update_ref(46, self.start_addr,
                               self.presetLabel1_7.currentIndex())
                ser.update_ref(47, self.start_addr,
                               self.presetLabel1_8.currentIndex())
                ser.update_ref(48, self.start_addr,
                               self.presetLabel1_9.currentIndex())
                ser.update_ref(49, self.start_addr,
                               self.presetLabel1_10.currentIndex())

                ser.update_ref(50, self.start_addr,
                               self.onoff1_1.currentIndex())
                ser.update_ref(51, self.start_addr,
                               self.onoff1_2.currentIndex())
                ser.update_ref(52, self.start_addr,
                               self.onoff1_3.currentIndex())
                ser.update_ref(53, self.start_addr,
                               self.onoff1_4.currentIndex())
                ser.update_ref(54, self.start_addr,
                               self.onoff1_5.currentIndex())
                ser.update_ref(55, self.start_addr,
                               self.onoff1_6.currentIndex())
                ser.update_ref(56, self.start_addr,
                               self.onoff1_7.currentIndex())
                ser.update_ref(57, self.start_addr,
                               self.onoff1_8.currentIndex())
                ser.update_ref(58, self.start_addr,
                               self.onoff1_9.currentIndex())
                ser.update_ref(59, self.start_addr,
                               self.onoff1_10.currentIndex())

                ser.update_ref(60, self.start_addr,
                               self.onoff2_1.currentIndex())
                ser.update_ref(61, self.start_addr,
                               self.onoff2_2.currentIndex())
                ser.update_ref(62, self.start_addr,
                               self.onoff2_3.currentIndex())
                ser.update_ref(63, self.start_addr,
                               self.onoff2_4.currentIndex())
                ser.update_ref(64, self.start_addr,
                               self.onoff2_5.currentIndex())
                ser.update_ref(65, self.start_addr,
                               self.onoff2_6.currentIndex())
                ser.update_ref(66, self.start_addr,
                               self.onoff2_7.currentIndex())
                ser.update_ref(67, self.start_addr,
                               self.onoff2_8.currentIndex())
                ser.update_ref(68, self.start_addr,
                               self.onoff2_9.currentIndex())
                ser.update_ref(69, self.start_addr,
                               self.onoff2_10.currentIndex())

                ser.update_ref(70, self.start_addr,
                               self.onoff3_1.currentIndex())
                ser.update_ref(71, self.start_addr,
                               self.onoff3_2.currentIndex())
                ser.update_ref(72, self.start_addr,
                               self.onoff3_3.currentIndex())
                ser.update_ref(73, self.start_addr,
                               self.onoff3_4.currentIndex())
                ser.update_ref(74, self.start_addr,
                               self.onoff3_5.currentIndex())
                ser.update_ref(75, self.start_addr,
                               self.onoff3_6.currentIndex())
                ser.update_ref(76, self.start_addr,
                               self.onoff3_7.currentIndex())
                ser.update_ref(77, self.start_addr,
                               self.onoff3_8.currentIndex())
                ser.update_ref(78, self.start_addr,
                               self.onoff3_9.currentIndex())
                ser.update_ref(79, self.start_addr,
                               self.onoff3_10.currentIndex())

                ser.update_ref(80, self.start_addr,
                               self.program_scene_fun1.currentIndex())

                self.write_text(ser, self.text_addr,
                                self.text_len, self.bank_name.text())

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

                self.set_dropdown(self.presetLabel1_1, 6,
                                  ser.get_ref(40, self.start_addr))
                self.set_dropdown(self.presetLabel1_2, 6,
                                  ser.get_ref(41, self.start_addr))
                self.set_dropdown(self.presetLabel1_3, 6,
                                  ser.get_ref(42, self.start_addr))
                self.set_dropdown(self.presetLabel1_4, 6,
                                  ser.get_ref(43, self.start_addr))
                self.set_dropdown(self.presetLabel1_5, 6,
                                  ser.get_ref(44, self.start_addr))
                self.set_dropdown(self.presetLabel1_6, 6,
                                  ser.get_ref(45, self.start_addr))
                self.set_dropdown(self.presetLabel1_7, 6,
                                  ser.get_ref(46, self.start_addr))
                self.set_dropdown(self.presetLabel1_8, 6,
                                  ser.get_ref(47, self.start_addr))
                self.set_dropdown(self.presetLabel1_9, 6,
                                  ser.get_ref(48, self.start_addr))
                self.set_dropdown(self.presetLabel1_10, 6,
                                  ser.get_ref(49, self.start_addr))

                self.set_dropdown(self.onoff1_1, 2,
                                  ser.get_ref(50, self.start_addr))
                self.set_dropdown(self.onoff1_2, 2,
                                  ser.get_ref(51, self.start_addr))
                self.set_dropdown(self.onoff1_3, 2,
                                  ser.get_ref(52, self.start_addr))
                self.set_dropdown(self.onoff1_4, 2,
                                  ser.get_ref(53, self.start_addr))
                self.set_dropdown(self.onoff1_5, 2,
                                  ser.get_ref(54, self.start_addr))
                self.set_dropdown(self.onoff1_6, 2,
                                  ser.get_ref(55, self.start_addr))
                self.set_dropdown(self.onoff1_7, 2,
                                  ser.get_ref(56, self.start_addr))
                self.set_dropdown(self.onoff1_8, 2,
                                  ser.get_ref(57, self.start_addr))
                self.set_dropdown(self.onoff1_9, 2,
                                  ser.get_ref(58, self.start_addr))
                self.set_dropdown(self.onoff1_10, 2,
                                  ser.get_ref(59, self.start_addr))

                self.set_dropdown(self.onoff2_1, 2,
                                  ser.get_ref(60, self.start_addr))
                self.set_dropdown(self.onoff2_2, 2,
                                  ser.get_ref(61, self.start_addr))
                self.set_dropdown(self.onoff2_3, 2,
                                  ser.get_ref(62, self.start_addr))
                self.set_dropdown(self.onoff2_4, 2,
                                  ser.get_ref(63, self.start_addr))
                self.set_dropdown(self.onoff2_5, 2,
                                  ser.get_ref(64, self.start_addr))
                self.set_dropdown(self.onoff2_6, 2,
                                  ser.get_ref(65, self.start_addr))
                self.set_dropdown(self.onoff2_7, 2,
                                  ser.get_ref(66, self.start_addr))
                self.set_dropdown(self.onoff2_8, 2,
                                  ser.get_ref(67, self.start_addr))
                self.set_dropdown(self.onoff2_9, 2,
                                  ser.get_ref(68, self.start_addr))
                self.set_dropdown(self.onoff2_10, 2,
                                  ser.get_ref(69, self.start_addr))

                self.set_dropdown(self.onoff3_1, 2,
                                  ser.get_ref(70, self.start_addr))
                self.set_dropdown(self.onoff3_2, 2,
                                  ser.get_ref(71, self.start_addr))
                self.set_dropdown(self.onoff3_3, 2,
                                  ser.get_ref(72, self.start_addr))
                self.set_dropdown(self.onoff3_4, 2,
                                  ser.get_ref(73, self.start_addr))
                self.set_dropdown(self.onoff3_5, 2,
                                  ser.get_ref(74, self.start_addr))
                self.set_dropdown(self.onoff3_6, 2,
                                  ser.get_ref(75, self.start_addr))
                self.set_dropdown(self.onoff3_7, 2,
                                  ser.get_ref(76, self.start_addr))
                self.set_dropdown(self.onoff3_8, 2,
                                  ser.get_ref(77, self.start_addr))
                self.set_dropdown(self.onoff3_9, 2,
                                  ser.get_ref(78, self.start_addr))
                self.set_dropdown(self.onoff3_10, 2,
                                  ser.get_ref(79, self.start_addr))

                self.set_dropdown(self.program_scene_fun1, 2,
                                  ser.get_ref(80, self.start_addr))

                bank = self.read_text(ser, self.text_addr, self.text_len)
                if bank == ' ' * self.text_len:
                    self.bank_name.setText("*" * self.text_len)
                else:
                    self.bank_name.setText(bank.strip())
                ser.close()

            except Exception as e:
                print(e)
        self.update_btn.clearFocus()

    def get_config(self):
        data = {}
        data["spinBox_PC1_1"] = self.spinBox_PC1_1.value()
        data["spinBox_PC1_2"] = self.spinBox_PC1_2.value()
        data["spinBox_PC1_3"] = self.spinBox_PC1_3.value()
        data["spinBox_PC1_4"] = self.spinBox_PC1_4.value()
        data["spinBox_PC1_5"] = self.spinBox_PC1_5.value()
        data["spinBox_PC1_6"] = self.spinBox_PC1_6.value()
        data["spinBox_PC1_7"] = self.spinBox_PC1_7.value()
        data["spinBox_PC1_8"] = self.spinBox_PC1_8.value()
        data["spinBox_PC1_9"] = self.spinBox_PC1_9.value()
        data["spinBox_PC1_10"] = self.spinBox_PC1_10.value()

        data["spinBox_CC1_1"] = self.spinBox_CC1_1.value()
        data["spinBox_CC1_1"] = self.spinBox_CC1_2.value()
        data["spinBox_CC1_3"] = self.spinBox_CC1_3.value()
        data["spinBox_CC1_4"] = self.spinBox_CC1_4.value()
        data["spinBox_CC1_4"] = self.spinBox_CC1_5.value()
        data["spinBox_CC1_6"] = self.spinBox_CC1_6.value()
        data["spinBox_CC1_7"] = self.spinBox_CC1_7.value()
        data["spinBox_CC1_8"] = self.spinBox_CC1_8.value()
        data["spinBox_CC1_8"] = self.spinBox_CC1_9.value()
        data["spinBox_CC1_10"] = self.spinBox_CC1_10.value()
        data["spinBox_CC2_1"] = self.spinBox_CC2_1.value()
        data["spinBox_CC2_2"] = self.spinBox_CC2_2.value()
        data["spinBox_CC2_3"] = self.spinBox_CC2_3.value()
        data["spinBox_CC2_4"] = self.spinBox_CC2_4.value()
        data["spinBox_CC2_5"] = self.spinBox_CC2_5.value()
        data["spinBox_CC2_6"] = self.spinBox_CC2_6.value()
        data["spinBox_CC2_7"] = self.spinBox_CC2_7.value()
        data["spinBox_CC2_8"] = self.spinBox_CC2_8.value()
        data["spinBox_CC2_9"] = self.spinBox_CC2_9.value()
        data["spinBox_CC2_10"] = self.spinBox_CC2_10.value()
        data["spinBox_CC3_1"] = self.spinBox_CC3_1.value()
        data["spinBox_CC3_2"] = self.spinBox_CC3_2.value()
        data["spinBox_CC3_3"] = self.spinBox_CC3_3.value()
        data["spinBox_CC3_4"] = self.spinBox_CC3_4.value()
        data["spinBox_CC3_5"] = self.spinBox_CC3_5.value()
        data["spinBox_CC3_6"] = self.spinBox_CC3_6.value()
        data["spinBox_CC3_7"] = self.spinBox_CC3_7.value()
        data["spinBox_CC3_8"] = self.spinBox_CC3_8.value()
        data["spinBox_CC3_9"] = self.spinBox_CC3_9.value()
        data["spinBox_CC3_10"] = self.spinBox_CC3_10.value()
        data["presetLabel1_1"] = self.presetLabel1_1.currentIndex()
        data["presetLabel1_2"] = self.presetLabel1_2.currentIndex()
        data["presetLabel1_3"] = self.presetLabel1_3.currentIndex()
        data["presetLabel1_4"] = self.presetLabel1_4.currentIndex()
        data["presetLabel1_5"] = self.presetLabel1_5.currentIndex()
        data["presetLabel1_6"] = self.presetLabel1_6.currentIndex()
        data["presetLabel1_7"] = self.presetLabel1_7.currentIndex()
        data["presetLabel1_8"] = self.presetLabel1_8.currentIndex()
        data["presetLabel1_8"] = self.presetLabel1_9.currentIndex()
        data["presetLabel1_10"] = self.presetLabel1_10.currentIndex()

        data["onoff1_1"] = self.onoff1_1.currentIndex()
        data["onoff1_2"] = self.onoff1_2.currentIndex()
        data["onoff1_3"] = self.onoff1_3.currentIndex()
        data["onoff1_4"] = self.onoff1_4.currentIndex()
        data["onoff1_5"] = self.onoff1_5.currentIndex()
        data["onoff1_6"] = self.onoff1_6.currentIndex()
        data["onoff1_7"] = self.onoff1_7.currentIndex()
        data["onoff1_8"] = self.onoff1_8.currentIndex()
        data["onoff1_9"] = self.onoff1_9.currentIndex()
        data["onoff1_10"] = self.onoff1_10.currentIndex()
        data["onoff2_1"] = self.onoff2_1.currentIndex()
        data["onoff2_2"] = self.onoff2_2.currentIndex()
        data["onoff2_3"] = self.onoff2_3.currentIndex()
        data["onoff2_4"] = self.onoff2_4.currentIndex()
        data["onoff2_5"] = self.onoff2_5.currentIndex()
        data["onoff2_6"] = self.onoff2_6.currentIndex()
        data["onoff2_7"] = self.onoff2_7.currentIndex()
        data["onoff2_8"] = self.onoff2_8.currentIndex()
        data["onoff2_8"] = self.onoff2_9.currentIndex()
        data["onoff2_10"] = self.onoff2_10.currentIndex()
        data["onoff3_1"] = self.onoff3_1.currentIndex()
        data["onoff3_2"] = self.onoff3_2.currentIndex()
        data["onoff3_3"] = self.onoff3_3.currentIndex()
        data["onoff3_4"] = self.onoff3_4.currentIndex()
        data["onoff3_5"] = self.onoff3_5.currentIndex()
        data["onoff3_6"] = self.onoff3_6.currentIndex()
        data["onoff3_7"] = self.onoff3_7.currentIndex()
        data["onoff3_8"] = self.onoff3_8.currentIndex()
        data["onoff3_9"] = self.onoff3_9.currentIndex()
        data["onoff3_10"] = self.onoff3_10.currentIndex()
        data["onoff3_10"] = self.program_scene_fun1.currentIndex()

        data["bank_name"] = self.bank_name.text()

        return data

    def set_config(self, data):
        for key, value in data.items():
            obj = eval(f'self.{key}')
            if isinstance(obj, QtWidgets.QLineEdit):
                obj.setText(value)
            elif isinstance(obj, QtWidgets.QSpinBox):
                obj.setValue(value)
            elif isinstance(obj, QtWidgets.QComboBox):
                obj.setCurrentIndex(value)

    def set_port(self, port):
        self.port = port
