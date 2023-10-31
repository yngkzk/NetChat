import typing
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal
from PyQt6 import QtGui, uic
from logger import log
from message import Message

class MainWindow(QMainWindow): 
    sendMessage = pyqtSignal(str)

    def __init__(self, username): 
        super().__init__() 
        uic.loadUi("gui/main_window.ui", self)
        #VN: стили можно подгружать здесь, в конструкторе каждого окна отдельно, а можно в main.py ко всему приложению
        self.username = username
        self.contact_list = []

    def show(self):
        super().show()
        button = self.findChild(QPushButton, "Send")
        button.clicked.connect(self.send_message)
        self.add_contact("General")

    def send_message(self):
        log.d("Кнопка нажата")
        textEdit = self.findChild(QTextEdit, "MessageToSend")
        message = textEdit.toPlainText()
        self.sendMessage.emit(message)
        textEdit.clear()

    #VN: Чтобы отправлять сообщение по нажатию Enter, дополните обработчик нажатия клавиш:
    # def keyPressEvent(self, ev):
    #         if ev.key() == ... :
    #              ...
    #     return super().keyPressEvent(ev)

    def show_message(self, message: Message):
        display = self.findChild(QTextBrowser, "MessageDisplay")
        log.d(message.senderName)
        display.append(f"[{message.time}]  <{message.senderName}>:    {message.text}")
        #VN: есть ещё метод display.setHtml(), и тогда можно аппендить текст с тегами и стилями

    def add_contact(self, name_contact): 
        contactList = self.findChild(QVBoxLayout, "ContactList")
        newContact = QLabel(text=name_contact)
        #VN: и тут в качестве слота для сигнала clicked (которого нет у QLabel), можно сразу указать лямбду,
        # которая сделает emit сигнала changeChat (его ещё надо будет пробросить через класс Gui)
        contactList.addWidget(newContact)
        self.contact_list.append(name_contact)
