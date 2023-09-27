import sys
from PyQt6.QtWidgets import QApplication
from router import Router
from logger import Logger


if __name__ == '__main__':
    app = QApplication(sys.argv)

    log = Logger(Logger.DEBUG)
    router = Router()
    router.start()

    app.exec()
