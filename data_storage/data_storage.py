import hashlib 
import json
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
            with open('data_storage/users.json', 'r') as json_file:
                for line in json_file:
                    user = json.loads(line)
                    if hashlib.md5(username.encode("UTF-8")).hexdigest() == user["username"] and hashlib.md5(password.encode("UTF-8")).hexdigest() == user["password"]:
                        self.authOk.emit(username)
                        return

            self.authBad.emit("Неправильное имя или пароль!")
        
    def register(self, email, username, password): 
        email_hash =  hashlib.md5(email.encode("UTF-8"))
        email_hash_result = email_hash.hexdigest()

        username_hash = hashlib.md5(username.encode("UTF-8"))
        username_hash_result = username_hash.hexdigest()

        password_hash = hashlib.md5(password.encode("UTF-8"))
        password_hash_result = password_hash.hexdigest()

        user = {"email": email_hash_result, "username": username_hash_result, "password": password_hash_result}
        self.authOk.emit(username)

        with open('data_storage/users.json', 'a') as json_file:
            json_file.write('\n')
            json.dump(user, json_file)
