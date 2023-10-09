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
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # self.server_address = ('localhost', 9900)
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
                if message.type in ("public", "service_request"):
                    adress = ('255.255.255.255', 9900)
                    self.server_socket.sendto(string_to_send.encode(), adress)
                elif message.senderIP:
                    adress = (message.senderIP, 9900)
                    self.server_socket.sendto(string_to_send.encode(), adress)
                self.sent.emit(message)
            else:
                time.sleep(0.025)

    def send(self, message: Message):
        self.lock.acquire()
        log.i('Сообщение доставлено')
        self.queue.append(message)
        self.lock.release()
    
