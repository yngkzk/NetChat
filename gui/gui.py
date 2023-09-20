from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import *
from PyQt6 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/main.ui", self)


class Gui(QThread):
    send_message = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        # self.window = MainWindow()     # На этом месте мой код умирает
        # self.window.show()

    def start(self):
        print('GUI has been launched!')
        # button = self.window.findChild(QPushButton, 'pushbutton')
        # button.clicked.connect(self.sendMessage)

    def sendMessage(self):
        print('Button pressed')
        # textedit = self.window.findChild(QTextEdit, 'MessageToSend')
        # message = textedit.toPlainText()
        # self.send_message.emit(message)
        # textedit.clear()


if __name__ == '__main__':
    gui = Gui()
    gui.start()
