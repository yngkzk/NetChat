import typing
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QKeyEvent
from PyQt6 import QtGui, uic
from logger import log
from message import Message


class MainWindow(QMainWindow):
    sendMessage = pyqtSignal(str)

    def __init__(self, username):
        super().__init__()
        uic.loadUi("GUI/main_window.ui", self)
        # VN: стили можно подгружать здесь, в конструкторе каждого окна отдельно, а можно в main.py ко всему приложению
        self.username = username
        self.contact_list = []

    def show(self):
        super().show()
        button = self.findChild(QPushButton, "Send")
        button.clicked.connect(self.send_message)
        self.add_contact("General")

        self.textEdit = self.findChild(QTextEdit, "MessageToSend")
        self.textEdit.installEventFilter(self)

        self.nicknameLabel = self.findChild(QLabel, "nicknameLabel")
        self.nicknameLabel.setText(self.username)

        self.smileMenu = self.findChild(QPushButton, 'emojiButton')
        self.smileMenu.clicked.connect(self.smile_menu)

    def send_message(self):
        log.d("Кнопка нажата")
        textEdit = self.findChild(QTextEdit, "MessageToSend")
        message = textEdit.toPlainText()
        self.sendMessage.emit(message)
        textEdit.clear()

    def eventFilter(self, obj, event):
        if obj == self.textEdit and event.type() == QKeyEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_Return and event.modifiers() == Qt.KeyboardModifier.NoModifier:
                self.send_message()
                return True
        return super().eventFilter(obj, event)

    def show_message(self, message: Message):
        display = self.findChild(QTextBrowser, "MessageDisplay")
        log.d(message.senderName)

        if message.senderName == self.username:
            text = f'<p style="margin-bottom: 10px; color: green;">[{message.time}]  <{message.senderName}>:    {message.text}</p>'
        else:
            text = f'<p style="margin-bottom: 10px;">[{message.time}]  <{message.senderName}>:    {message.text}</p>'

        message_text = text.replace('\n', '<br>')
        display.append(message_text)

    def add_contact(self, name_contact):
        contactList = self.findChild(QVBoxLayout, "ContactList")
        newContact = QLabel(text=name_contact)
        # VN: и тут в качестве слота для сигнала clicked (которого нет у QLabel), можно сразу указать лямбду,
        # которая сделает emit сигнала changeChat (его ещё надо будет пробросить через класс Gui)
        contactList.addWidget(newContact)
        self.contact_list.append(name_contact)

    # def create_smile_menu(self):
    #     log.i('Smile Menu OPEN')
    #
    #     smiles = [
    #         ["\U0001f600"], ["\U0001f601"], ["\U0001f602"]
    #     ]
    #
    #     smilesLayout = QGridLayout()
    #
    #     for i, j, row, col in smiles:
    #         a = QPushButton(i)
    #         a.setFixedSize(15, 15)
    #         a.setStyleSheet('background: rgba(0,0,0,0); border: none;')
    #         smilesLayout.addWidget(a, row, col)
    #         a.clicked.connect(lambda s, j=j: self.textEdit.insertPlainText(chr(j)))
    #
    #     return smilesLayout
    #
    # def smile_menu(self):
    #     super.__init__()
    #     mainLayout = QVBoxLayout()
    #     self.setLayout(mainLayout)
    #
    #     self.main_display = QLabel(text="0")
    #     self.main_display.setFixedHeight(15)
    #     self.main_display.setAlignment(Qt.AlignmentFlag.AlignRight)
    #     mainLayout.addWidget(self.main_display)
    #
    #     mainLayout.addLayout(self.create_smile_menu())