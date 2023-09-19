from PyQt6.QtCore import QThread, pyqtSignal
import socket 

class MessageReceiver(QThread):
    messageReceived = pyqtSignal(str, str)

    def __init__(self, port):
        super().__init__()
        self.port = port 
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('localhost', self.port)
        self.server_socket.bind(self.server_address)
        self.is_running = False 

    def start(self):
        print('UDPReceiver has been launched!')

        self.is_running = True 
        while self.is_running: 
            data, addr = self.server_socket.recvfrom(1024)
            message = data.decode(encoding='utf-8') 
            print(f"Message received from {addr}: {message}")
            response = "OK"
            self.server_socket.sendto(response.encode("utf-8"), addr)
        
    def stop(self): 
        self.is_running = False 
        self.server_socket.close() 
        print("UDP_Receiver is stopping!")


if __name__ == "__main__": 
    port = 9900
    udp_server = MessageReceiver(port)
    udp_server.start() 
    udp_server.stop() 
