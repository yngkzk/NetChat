from PyQt6.QtCore import QThread, pyqtSignal
import socket
from logger import log
import time
import threading


class MessageSender(QThread):
    queue = []
    sent = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('localhost', 9900)
        self.running = False
        self.lock = threading.Lock()

    def run(self):  # Вкратце, я этот метод назвал start, тем самым переписав метод QThread
        log.i('UDPSender has been launched!')
        log.i('Дошел до участка кода "MessageSender - RUN".')
        self.running = True
        while self.running:
            if len(self.queue) > 0:
                log.i('И тут тоже все нормально')
                self.lock.acquire()
                message, message_type = self.queue.pop()
                self.lock.release()

                self.server_socket.sendto(message.encode(), self.server_address)
                self.sent.emit(message)
            else:
                time.sleep(0.025)

    def send(self, message, message_type):
        self.lock.acquire()
        log.i('Сообщение доставлено')
        self.queue.append((message, message_type))
        self.lock.release()
