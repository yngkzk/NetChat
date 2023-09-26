from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal
from PyQt6 import uic
from logger import log


class MainWindow(QMainWindow): 
    sendMessage = pyqtSignal(str, str)

    def __init__(self, username): 
        super().__init__() 
        uic.loadUi("GUI\main_window.ui", self)
        self.username = username

    def show(self):
        super().show()
        button = self.findChild(QPushButton, "Send")
        button.clicked.connect(self.send_message)

    def send_message(self):
        log.d("Кнопка нажата")
        textEdit = self.findChild(QTextEdit, "MessageToSend")
        message = textEdit.toPlainText()
        self.sendMessage.emit(message, 'public')
        textEdit.clear() 

    def show_message(self, message, message_type):
        display = self.findChild(QTextBrowser, "MessageDisplay")
        display.append(message)

