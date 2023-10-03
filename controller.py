from PyQt6.QtCore import QObject, pyqtSignal
from logger import log 
from message import Message


class Controller(QObject):
    switchWindow = pyqtSignal(str, str)
    addContact = pyqtSignal(str)
    showMessage = pyqtSignal(Message)
    sendMessage = pyqtSignal(Message)
    setChat = pyqtSignal(str)

    _username = 'John Doe'
    _state = "INIT" 
    _transitions = (
        {"from": "INIT",          "to": "LOGIN",          "by": "DB_READY"}, 
        {"from": "LOGIN",         "to": "AUTH",           "by": "GUI_LOGIN"}, 
        {"from": "AUTH",          "to": "MAIN_WIN",       "by": "DB_AUTH_OK"},
        {"from": "AUTH",          "to": "LOGIN",          "by": "DB_AUTH_BAD"},  

        {"from": "MAIN_WIN",      "to": "ADD_FRIEND",     "by": "UR_HELLO"},  
        {"from": "ADD_FRIEND",    "to": "MAIN_WIN",       "by": "IMMEDIATELY"},  

        {"from": "MAIN_WIN",      "to": "CHECK_MSG",      "by": "UR_MESSAGE"},  
        {"from": "CHECK_MSG",     "to": "MAIN_WIN",       "by": "IMMEDIATELY"},  

        {"from": "MAIN_WIN",      "to": "SEND_MSG",       "by": "GUI_SEND"},  
        {"from": "SEND_MSG",      "to": "MAIN_WIN",       "by": "IMMEDIATELY"},  

        {"from": "MAIN_WIN",      "to": "CHANGING_CHAT",  "by": "GUI_CHAT_CHANGE"},  
        {"from": "CHANGING_CHAT", "to": "MAIN_WIN",       "by": "IMMEDIATELY"}
    )

    def __init__(self):
        super().__init__()
        self._process_state("INIT")

    def _process_state(self, *args):
        match self._state: 
            case "INIT":
                pass

            case "LOGIN":
                self.switchWindow.emit("LoginWindow", "")

            case "AUTH":
                pass

            case "MAIN_WIN":
                if args:
                    self._username = args[0]
                self.switchWindow.emit("MainWindow", self._username)

            case "ADD_FRIEND":
                friendname = args[0]
                self.addContact.emit(friendname)

            case "CHECK_MSG": 
                message: Message = args[0]

                if message.type == "public": 
                    self.showMessage.emit(message)

            case "SEND_MSG":
                message_text = args[0]
                message = Message('{"text": "%s"}' % message_text)
                message.senderName = self._username
                message.type = 'public'
                self.sendMessage.emit(message)
            
            case "CHANGING_CHAT": 
                chat_name = args[0]
                self.setChat.emit(chat_name)

            case _:
                log.w("Unknown State!")
            
    def _process_signal(self, signal_name, *args): 
        allowed_transitions = list(filter(lambda dict: dict["from"] == self._state and dict["by"] == signal_name, self._transitions))
        if len(allowed_transitions) == 0: 
            return 

        current_transition = allowed_transitions[0]
        self._state = current_transition["to"]
        log.d(f"Переключились из {current_transition['from']} в {self._state}, по сигналу {signal_name}")

        self._process_state(*args) 
        allowed_transitions = list(filter(lambda dict: dict["from"] == self._state and dict["by"] == "IMMEDIATELY", self._transitions))
        if len(allowed_transitions) == 0: 
            return 

        current_transition = allowed_transitions[0]
        self._state = current_transition["to"]
        log.d(f"Переключились из {current_transition['from']} в {self._state}, по сигналу IMMEDIATELY")

        self._process_state() 


    def database_ready(self):
        self._process_signal('DB_READY')

    def login(self, username):
        if username:
            self._process_signal('GUI_LOGIN', username)

    def database_auth_ok(self, username):
        self._process_signal("DB_AUTH_OK", username)

    def database_auth_bad(self, error_text):
        self._process_signal("DB_AUTH_BAD", error_text)

    def received_hello(self, username):
        self._process_signal("UR_HELLO", username)

    def received_message(self, message):
        self._process_signal("UR_MESSAGE", message)

    def send_message(self, message_text):
        self._process_signal("GUI_SEND", message_text)

    def change_chat(self, chat_name):
        self._process_signal("GUI_CHAT_CHANGE", chat_name)

