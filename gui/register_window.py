from logger import log
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal
import re 


class RegisterWindow(QDialog):
    loginUser = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/register_window.ui", self)
        
    def show(self):
        super().show()
        button = self.findChild(QPushButton, "Register")
        button.clicked.connect(self.login_user)
    
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)

    def login_user(self):
        email_input = self.findChild(QLineEdit, "Email")
        name_input = self.findChild(QLineEdit, "Nickname")
        password_input = self.findChild(QLineEdit, "Password")
        confirmPassword_input = self.findChild(QLineEdit, "ConfirmPassword")

        user_email = email_input.text()
        user_name = name_input.text()
        user_password = password_input.text()
        user_confirmPassword = confirmPassword_input.text()

        if (self.is_valid_email(user_email)) and user_name and (len(user_password) > 7) and (any(char.isalpha() for char in user_password) and any(char.isdigit() for char in user_password) and re.search(r'[!@#$%^&*()_+={}\[\]:;"\'<>,.?\\|]', user_password)) and (user_password == user_confirmPassword):
            self.loginUser.emit(user_name, user_password)
            log.i(f"Пользователь '{user_name}' авторизован")