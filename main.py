import sys
from PyQt6.QtWidgets import QApplication
from router import Router
from logger import Logger


if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open('stylesheet/style.css', 'r', encoding='utf-8') as style:
        settings = style.read()
        print(settings)
    app.setStyleSheet(settings)

    log = Logger(Logger.DEBUG)
    router = Router()
    router.start()

    app.exec()
