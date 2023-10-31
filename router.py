from PyQt6.QtCore import QObject
from data_storage import DataStorage
from gui import GUI
from udp_sender import MessageSender
from udp_receiver import MessageReceiver
from controller import Controller
from logger import log

class Router(QObject):
    def __init__(self):
        super().__init__()
        self.data_storage = DataStorage()
        self.GUI = GUI()
        self.udp_receiver = MessageReceiver()
        self.udp_sender = MessageSender()
        self.controller = Controller() 

        # Сигналы GUI
        self.GUI.loginUser.connect(self.data_storage.auth)
        self.GUI.loginUser.connect(self.controller.login)
        self.GUI.sendMessage.connect(self.controller.send_message)
        self.GUI.changeChat.connect(self.controller.change_chat)

        # Сигналы Controller
        self.controller.switchWindow.connect(self.GUI.set_window)
        self.controller.addContact.connect(self.GUI.add_contact)
        self.controller.showMessage.connect(self.GUI.show_message)
        self.controller.sendMessage.connect(self.udp_sender.send)
        self.controller.setChat.connect(self.GUI.set_chat)
        self.controller.sendHello.connect(self.udp_sender.send)

        # Сигналы UDP_Receiver
        self.udp_receiver.message.connect(self.controller.received_message)
        self.udp_receiver.hello.connect(self.controller.received_hello)

        # Сигналы DataStorage
        self.data_storage.ready.connect(self.controller.database_ready)
        self.data_storage.authOk.connect(self.controller.database_auth_ok)
        self.data_storage.authBad.connect(self.controller.database_auth_bad)

    def start(self):
        log.i("Router has been launched!")
        self.data_storage.start()
        self.GUI.start()
        self.udp_receiver.start()
        self.udp_sender.start()


    def stop(self):
        self.udp_receiver.stop()
        self.udp_sender.stop()
        self.GUI.stop()
        self.data_storage.stop()

