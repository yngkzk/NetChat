from PyQt6.QtCore import QThread, pyqtSignal
from logger import log

class DataStorage(QThread):
    username = None 
    ready = pyqtSignal()
    authOk = pyqtSignal(str)
    authBad = pyqtSignal()
    valid_username = "user"
    valid_password = "password"

    def run(self):
        log.i('DataStorage has been launched!')
        self.ready.emit()

    def auth(self, username):
        self.username = username

    def login(self, username, password):
        if username == self.valid_username and password == self.valid_password:
            self.authOk.emit(username)
        else:
            self.authBad.emit()


