from PyQt6.QtWidgets import *
from gui import GUI

class LoginDialog(QDialog):
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

        self.gui_service = GUI() 

    def login(self):
        username = self.username_input.text()
        if username:
            # Отправляем имя пользователя в сервис GUI
            self.gui_service.handle_username(username)
            self.accept()  # Закрываем окно входа
        else:
            print("Имя пользователя не введено.")