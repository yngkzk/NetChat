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
        self.GUI.sendMessage.connect(self.udp_sender.send)

        # Сигналы Controller
        self.controller.switchWindow.connect(self.GUI.set_window)

        # Сигналы UDP_Receiver
        self.udp_receiver.message.connect(self.controller.message_receiver)
        

    def start(self):
        log.i("Router has been launched!")
        self.data_storage.start()
        self.GUI.start()
        self.udp_sender.start()
        self.udp_receiver.start()

    def stop(self):
        self.udp_receiver.stop()
        self.udp_sender.stop()
        self.GUI.stop()
        self.data_storage.stop()

