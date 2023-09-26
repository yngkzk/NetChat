from PyQt6.QtCore import QThread, pyqtSignal
import socket
from logger import log


class MessageReceiver(QThread): 
    message = pyqtSignal(str, str)

    def __init__(self, port=9900):
        super().__init__()
        self.port = port
        self.server_address = ('localhost', self.port)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.is_enabled = False

    def start(self):
        log.i('UDPReceiver has been launched!')
        self.server_socket.bind(self.server_address)
        self.is_enabled = True 

        while self.is_enabled:
            data, client_address = self.server_socket.recvfrom(4096)
            message = data.decode(encoding="UTF-8")
            log.d(f'Message received from {client_address}: {message}')

            # reply_message = 'OK'
            # self.server_socket.sendto(reply_message.encode(), client_address)

            self.message.emit(message, 'public')

    def stop(self):
        print('UDPReceiver is stopping...')
        self.is_enabled = False
        super().stop()



if __name__ == '__main__':
    my_server = MessageReceiver(9900)
    my_server.start()
    my_server.stop()
