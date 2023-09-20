from PyQt6.QtCore import QObject
# from logger import Logger
from data_storage import DataStorage
from GUI import GUI
from udp_sender import MessageSender
from udp_receiver import MessageReceiver


# log = Logger(Logger.DEBUG)


class Router(QObject):
    def __init__(self):
        super().__init__()
        self.data_storage = DataStorage()
        self.GUI = GUI()
        self.udp_receiver = MessageReceiver()
        self.udp_sender = MessageSender()

        self.GUI.sendMessage.connect(lambda s: print(s))

    def start(self):
        self.data_storage.start()
        self.GUI.start()
        self.udp_sender.start()
        self.udp_receiver.start()

    def stop(self):
        self.udp_receiver.stop()
        self.udp_sender.stop()
        self.GUI.stop()
        self.data_storage.stop()

