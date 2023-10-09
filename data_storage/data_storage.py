from PyQt6.QtCore import QThread, pyqtSignal
from logger import log

class DataStorage(QThread):
    username = None
    password = None
    ready = pyqtSignal()
    authOk = pyqtSignal(str)
    authBad = pyqtSignal(bool)
    valid_username = "user"
    valid_password = "password"

    def run(self):
        log.i('DataStorage has been launched!')
        self.ready.emit()

    def auth(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        log.i('DataStorage is checking login...')
        if username == self.valid_username and password == self.valid_password:
            self.authOk.emit(username)
        else:
            self.authBad.emit(True)


