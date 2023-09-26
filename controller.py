from PyQt6.QtCore import QObject, pyqtSignal
from logger import log 

class Controller(QObject):
    switchWindow = pyqtSignal(str, str)

    def login(self, username):
        if username: 
            self.switchWindow.emit("MainWindow", username) 
    
    def message_receiver(self, message_text, message_type):
        log.d(f"Сообщение получено '{message_text}' => {message_type}") 