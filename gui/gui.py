from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QMainWindow, QPushButton, QTextEdit
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal


class MainWindow(QMainWindow): 
    def __init__(self):
        super().__init__() 
        uic.loadUi("GUI\main.ui", self)

class GUI(QThread):
    sendMessage = pyqtSignal(str)

    def __init__(self):
        super().__init__() 
        self.window = MainWindow()  
        self.window.show() 

    def run(self): 
        print("GUI runned!")  

        button = self.window.findChild(QPushButton, "Send")
        button.clicked.connect(self.send_message)

    def send_message(self): 
        print("Кнопка нажата!")

        textEdit = self.window.findChild(QTextEdit, "MessageToSend")
        message = textEdit.toPlainText() 

        self.sendMessage.emit(message)
        