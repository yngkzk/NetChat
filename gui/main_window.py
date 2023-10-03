from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal
from PyQt6 import uic
from logger import log
from message import Message

class MainWindow(QMainWindow): 
    sendMessage = pyqtSignal(str)

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
        self.sendMessage.emit(message)
        textEdit.clear() 

    def show_message(self, message: Message):
        display = self.findChild(QTextBrowser, "MessageDisplay")
        display.append(f"[{message.time}]  <{message.senderName}>:    {message.text}")

