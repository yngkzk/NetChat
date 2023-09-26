from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal
from PyQt6 import uic


class MainWindow(QMainWindow): 
    sendMessage = pyqtSignal(str)

    def __init__(self, username): 
        super().__init__() 
        uic.loadUi("GUI\main.ui", self)
        self.username = username

    def show(self):
        super().show()
        button = self.findChild(QPushButton, "Send")
        button.clicked.connect(self.send_message)

    def send_message(self):
        textEdit = self.findChild(QTextEdit, "MessageToSend")
        message = textEdit.toPlainText()
        self.sendMessage.emit(message)


