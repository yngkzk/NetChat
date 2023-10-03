from PyQt6.QtCore import QThread, pyqtSignal
import socket
from logger import log
import time
import threading
from message import Message
from datetime import datetime

class MessageSender(QThread):
    queue = []
    sent = pyqtSignal(Message)

    def __init__(self):
        super().__init__()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('localhost', 9900)
        self.running = False
        self.lock = threading.Lock()

    def run(self): 
        log.i('UDPSender has been launched!')
        self.running = True
        message: Message = None 

        while self.running:
            if len(self.queue) > 0:
                self.lock.acquire()
                message = self.queue.pop()
                self.lock.release()
                message.time = datetime.now().strftime("%H:%M:%S")
                string_to_send = message.toJson()
                self.server_socket.sendto(string_to_send.encode(), self.server_address)
                self.sent.emit(message)
            else:
                time.sleep(0.025)

    def send(self, message: Message):
        self.lock.acquire()
        log.i('Сообщение доставлено')
        self.queue.append(message)
        self.lock.release()
