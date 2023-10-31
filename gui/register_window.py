from logger import log
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal, Qt
import re 


class RegisterWindow(QDialog):
    registerUser = pyqtSignal(str, str, str)

    def __init__(self):
        super().__init__()
        log.i("Создание окна регистрации...")
        uic.loadUi("GUI/register_window.ui", self)
        
    def show(self):
        super().show()
        button = self.findChild(QPushButton, "Register")
        button.clicked.connect(self.register_user)

        self.email_input = self.findChild(QLineEdit, "Email")
        self.name_input = self.findChild(QLineEdit, "Nickname")
        self.password_input = self.findChild(QLineEdit, "Password")
        self.confirmPassword_input = self.findChild(QLineEdit, "ConfirmPassword")
        self.errorLabel = self.findChild(QLabel, "ErrorLabel")
    
    def is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)

    def is_valid_password(self, password):
        if len(password) < 7:
            return False
        return re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@#$%^!&*])[A-Za-z\d@#$%^!&*]+$', password)

    def register_user(self):
        user_email = self.email_input.text()
        user_name = self.name_input.text()
        user_password = self.password_input.text()
        user_confirmPassword = self.confirmPassword_input.text()

        if user_email and user_name and user_password and user_confirmPassword: 
            if not self.is_valid_email(user_email):
                QMessageBox.critical(None, "Ошибка", "<p style='color: red; font-size: 20px;'>Неправильный формат email!</p>")
            elif not self.is_valid_password(user_password):
                QMessageBox.critical(None, "Ошибка", "<p style='color: red; font-size: 20px;'>Пароль не соответствует требованиям!</p>")
            elif user_password != user_confirmPassword:
                QMessageBox.critical(None, "Ошибка", "<p style='color: red; font-size: 20px;'>Пароли не совпадают</p>")
            else:
                self.registerUser.emit(user_email, user_name, user_password)
                log.i(f"Пользователь '{user_name}' зарегистрирован")
                QMessageBox.information(None, "Успешная регистрация", f"<p style='color: green; font-size: 20px;'>Пользователь '{user_name}' зарегистрирован</p>")
        else:
            QMessageBox.critical(None, "Ошибка", "<p style='color: red; font-size: 20px;'>Заполните все поля!</p>")