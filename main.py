import sys
from PyQt6.QtWidgets import QApplication
from router import Router
from logger import Logger


if __name__ == '__main__':
    router = Router()
    log = Logger(Logger.DEBUG)
    router.start()

    app = QApplication(sys.argv)
    app.exec()

