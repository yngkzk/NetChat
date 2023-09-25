from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal
from logger import log

class LoginWindow(QDialog):
    loginUser = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вход")
        self.setGeometry(100, 100, 300, 100)

        layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Введите имя пользователя")
        layout.addWidget(self.username_input)

        login_button = QPushButton("Войти", self)
        login_button.clicked.connect(self.login)
        layout.addWidget(login_button)

        self.setLayout(layout)

        with open("gui/style.css", "r", encoding='utf-8') as file: 
            self.setStyleSheet(file.read())

    def login(self):
        username = self.username_input.text()
        if username:
            log.i(f"Пользователь {username} вошел.")
            self.loginUser.emit(username)
        else:
            print("Имя пользователя не введено.")
    
