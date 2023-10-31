from logger import log
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal


class LoginWindow(QDialog):
    loginUser = pyqtSignal(str, str)
    registerWindow = pyqtSignal()

    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/login_window.ui", self)
        
    def show(self):
        super().show()
        loginButton = self.findChild(QPushButton, "Login")
        loginButton.clicked.connect(self.login_user)

        registerButton = self.findChild(QPushButton, "Register")
        registerButton.clicked.connect(self.showRegisterWindow)

    def login_user(self):
        name_input = self.findChild(QLineEdit, "Nickname")
        login_input = self.findChild(QLineEdit, "Password")
        user_name = name_input.text()
        user_password = login_input.text()
        if user_name and user_password:
            self.loginUser.emit(user_name, user_password)
            log.i(f"Пользователь '{user_name}' авторизован")

    def showRegisterWindow(self): 
        log.i("Открытие окна регистрации!")
        self.registerWindow.emit()
    
    def show_auth_error(self, error_message):
        QMessageBox.critical(None, "Ошибка авторизации", f"<p style='color: red; font-size: 20px;'>{error_message}</p>")