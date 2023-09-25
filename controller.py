from PyQt6.QtCore import QObject, pyqtSignal

class Controller(QObject):
    switchWindow = pyqtSignal(str, str)

    def login(self, username):
        if username: 
            self.switchWindow.emit("MainWindow", username) 
            