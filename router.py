from PyQt6.QtCore import QObject
from data_storage import DataStorage
from gui import Gui
from udp_sender import MessageSender
from udp_receiver import MessageReceiver
from logger import Logger


log = Logger(Logger.DEBUG)


class Router(QObject):
    def __init__(self):
        super().__init__()
        self.data_storage = DataStorage()
        self.gui = Gui()
        self.udp_receiver = MessageReceiver()
        self.udp_sender = MessageSender()

        # Роутить тут

    def start(self):
        global log
        log.d('Start')
        self.data_storage.start()
        self.gui.start()
        self.udp_sender.start()
        self.udp_receiver.start()

    def stop(self):
        self.udp_receiver.stop()
        self.udp_sender.stop()
        self.gui.stop()
        self.data_storage.stop()

