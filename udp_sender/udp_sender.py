from PyQt6.QtCore import QThread
import socket


class MessageSender(QThread):  # Ansar
    def __init__(self, address='127.0.0.1', port=9900):
        super().__init__()
        self.address = address
        self.port = port
        self.server_address = (self.address, self.port)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def start(self):
        print('UDPSender has been launched!')

    def send(self, text, type):
        message = f"{text} | TYPE - ({type})"
        self.server_socket.sendto(message.encode(), self.server_address)

    def receive(self):
        data, addr = self.server_socket.recvfrom(1024)
        print('Response from the server:', data.decode(encoding='UTF-8'), sep=' ')


if __name__ == '__main__':
    client = MessageSender()
    client.start()
    client.send('Hallo', 'simple-text')
