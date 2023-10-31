from PyQt6.QtCore import QThread, pyqtSignal
from logger import log

class DataStorage(QThread):
    username = None
    password = None
    ready = pyqtSignal()
    authOk = pyqtSignal(str)
    authBad = pyqtSignal(str)

    def run(self):
        log.i('DataStorage has been launched!')
        self.ready.emit()

    def auth(self, username, password):
        with open("data_storage/user.db", "r", encoding="UTF-8") as user_file: 
            user_data = user_file.read().split(' ')
        
            valid_username = user_data[0]
            valid_password = user_data[1]

        log.i('DataStorage is checking login...')
        if username == valid_username and password == valid_password:
            self.authOk.emit(username)
        else:
            self.authBad.emit("Неправильное имя или пароль!")

        
    def register(self): 
        pass 


