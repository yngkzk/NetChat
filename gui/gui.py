from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import *
from PyQt6 import uic
from login_dialog import LoginDialog

class MainWindow(QMainWindow): 
    def __init__(self):
        super().__init__() 
        uic.loadUi("GUI\main.ui", self)

class GUI(QThread):
    sendMessage = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.window = MainWindow()
        self.login_dialog = LoginDialog()  # Создаем экземпляр окна входа
        self.login_dialog.exec()  # Отображаем окно входа

        self.window.show()

        button = self.window.findChild(QPushButton, "Send")
        button.clicked.connect(self.send_message)

    def send_message(self):
        textEdit = self.window.findChild(QTextEdit, "MessageToSend")
        message = textEdit.toPlainText()
        self.sendMessage.emit(message)

    # Слот для обработки имени пользователя от окна входа
    def handle_username(self, username):
        print(f"Пользователь {username} вошел.")






        