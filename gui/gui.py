from logger import log
from PyQt6.QtCore import QObject
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget
from .main_window import MainWindow
from .login_window import LoginWindow
from .register_window import RegisterWindow
from message import Message

class GUI(QObject):
    sendMessage = pyqtSignal(str)
    show_message = pyqtSignal(Message)
    changeChat = pyqtSignal(str)
    add_contact = pyqtSignal(str)
    window : QWidget = None
    loginUser = pyqtSignal(str, str)
    registerUser = pyqtSignal(str, str, str)
    showRegisterWindow = pyqtSignal()
    authBad = pyqtSignal(str)
    
    

    def __init__(self):
        super().__init__()
        self.running = False

    def start(self):
        self.run()

    def run(self):
        log.i("GUI has been launched!")

    def set_window(self, window_name, username=None):
        log.d('Window:', window_name)



        if window_name == type(self.window).__name__:
            return  

        self.running = True
        if self.window is not None:
            self.window.hide()
        match window_name: 
            case 'MainWindow':
                self.window = MainWindow(username)
                self.show_message.connect(self.window.show_message)
                self.add_contact.connect(self.window.add_contact)
                self.window.sendMessage.connect(self.sendMessage)
            case 'LoginWindow':
                self.window = LoginWindow()
                self.window.loginUser.connect(self.loginUser)
                self.window.registerWindow.connect(self.showRegisterWindow)
                self.authBad.connect(self.window.show_auth_error)
            case 'RegisterWindow': 
                self.window = RegisterWindow()
                self.window.registerUser.connect(self.registerUser)
            case _:
                log.e('Неизвестное имя окна:', window_name)
        if self.running:
            self.window.show()

    def set_chat(self, name_chat):
        pass