from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QWidget
from .login_window import LoginWindow
from .main_window import MainWindow
from logger import log


class GUI(QThread):

    loginUser = pyqtSignal(str)
    window: QWidget = None

    def __init__(self):
        super().__init__()
        self.running = False 
        self.set_window("LoginWindow")
        
    
    def start(self): 
        self.run()

    def run(self):
        log.i("GUI has been launched!")
        self.window.show()
        self.running = True 
    
    def set_window(self, window_name, username=None): 
        if self.window is not None: 
            self.window.hide()

        match window_name:
            case "MainWindow":
                self.window = MainWindow(username)
                self.window.sendMessage.connect(self.loginUser)
            case "LoginWindow":
                self.window = LoginWindow()
                self.window.loginUser.connect(self.loginUser)
            case _:
                if self.running:
                    self.run()
        