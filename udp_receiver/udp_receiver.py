from PyQt6.QtCore import QThread, pyqtSignal
import socket
from logger import log


class MessageReceiver(QThread): 
    message = pyqtSignal(str, str)
    hello = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.server_address = ('localhost', 9900)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.is_enabled = False

    def run(self):
        log.i('UDPReceiver has been launched!')

        self.server_socket.bind(self.server_address)
        self.is_enabled = True

        while self.is_enabled:
            data, client_address = self.server_socket.recvfrom(1024)
            message = data.decode(encoding="UTF-8")
            log.d(f'Message received from {client_address}: {message}')

            self.message.emit(message, 'public')

    def stop(self):
        print('UDPReceiver is stopping...')
        self.is_enabled = False
        super().stop()

