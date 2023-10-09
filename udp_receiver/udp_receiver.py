from PyQt6.QtCore import QThread, pyqtSignal
import socket
from logger import log
from message import Message


class MessageReceiver(QThread): 
    message = pyqtSignal(Message)
    hello = pyqtSignal(Message)

    def __init__(self):
        super().__init__()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        self.server_address = (ip_address, 9900)
        self.is_enabled = False

    def run(self):
        log.i('UDPReceiver has been launched!')

        self.server_socket.bind(self.server_address)
        self.is_enabled = True

        while self.is_enabled:
            data, client_address = self.server_socket.recvfrom(4096)
            received_string = data.decode(encoding="UTF-8")
            message = Message(received_string) 
            message.senderIP = client_address[0]
            log.d(f'Message received from {client_address}: {received_string}')
            if message.type == "service_request" and message.text.lower() == "hello":
                self.hello.emit(message)
            else:
                self.message.emit(message)

    def stop(self):
        print('UDPReceiver is stopping...')
        self.is_enabled = False
        super().stop()

