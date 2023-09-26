# from PyQt6.QtCore import QThread, pyqtSlot
# import socket 

# class MessageSender(QThread):
#     def __init__(self, address='localhost', port=9900):
#         super().__init__()
#         self.address = address
#         self.port = port 
#         self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
#         self.server_address = (self.address, self.port)
    
#     def start(self):
#         print('UDPSender has been launched!')

#     @pyqtSlot(str, str)
#     def send(self, text, type):
#         message = f"{text} ({type})"
#         self.client_socket.sendto(message.encode('utf-8'), self.server_address)
    
#     def receive(self): 
#         data, addr = self.client_socket.recvfrom(1024)
#         response = data.decode("utf-8")
#         print('Response from the server:', response)

# if __name__ == "__main__": 
#     udp_client = MessageSender('localhost', 9900)
#     udp_client.start() 