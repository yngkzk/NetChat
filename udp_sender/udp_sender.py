from PyQt6.QtCore import QThread, pyqtSignal
import socket
from logger import log
import time
import threading

class MessageSender(QThread):  
    _queue = []
    sent = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('localhost', 9900)
        self.running = False
        self.lock =  threading.Lock()

    def start(self):
        log.i('UDPSender has been launched!')
        self.running = True 

        while self.running: 
            if len(self._queue) > 0: 
                self.lock.acquire()
                message, message_type = self._queue.pop()
                self.lock.release()

                self.server_socket.sendto(message.encode(), self.server_address)
                self.sent.emit(message)
            else:
                time.sleep(0.025)            

    def send(self, message, message_type):
        self.lock.acquire()
        self._queue.append((message, message_type, ))
        self.lock.release()




