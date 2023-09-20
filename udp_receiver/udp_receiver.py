from PyQt6.QtCore import QThread
import socket


class MessageReceiver(QThread):  # Ansar
    def start(self): 
        print("UDP_Receiver runned!")  


    # def __init__(self, port=9900):
    #     super().__init__()
    #     self.port = port
    #     self.server_address = ('127.0.0.1', self.port)
    #     self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #     self.server_socket.bind(self.server_address)
    #     self.is_enabled = True

    # def start(self):
    #     print('UDPReceiver has been launched!')
    #     while self.is_enabled:
    #         data, client_address = self.server_socket.recvfrom(1024)
    #         message = data.decode(encoding="UTF-8")
    #         print(f'Message received from {client_address}: {message}')
    #         reply_message = 'OK'
    #         self.server_socket.sendto(reply_message.encode(), client_address)

    # def stop(self, message):
    #     if message == 'exit':
    #         print('UDPReceiver is stopping...')
    #         self.is_enabled = False
    #         self.server_socket.close()
    #     else:
    #         return


if __name__ == '__main__':
    my_server = MessageReceiver(9900)
    my_server.start()
    my_server.stop()
