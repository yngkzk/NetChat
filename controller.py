from PyQt6.QtCore import QObject, pyqtSignal
from logger import log 

class Controller(QObject):
    switchWindow = pyqtSignal(str, str)
    addContact = pyqtSignal(str)
    showMessage = pyqtSignal(str)
    sendMessage = pyqtSignal(str, str)
    setChat = pyqtSignal(str)

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
        {"from": "GUI_SEND",      "to": "MAIN_WIN",       "by": "IMMEDIATELY"},  

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
                username = args[0]
                self.switchWindow.emit("MainWindow", username)

            case "ADD_FRIEND":
                friendname = args[0]
                self.addContact.emit(friendname)

            case "CHECK_MSG": 
                message_text = args[0]
                message_type = args[1]

                if message_type == "public": 
                    self.showMessage.emit(message_text)

            case "SEND_MSG":
                message_text = args[0]
                self.sendMessage.emit(message_text, "public")
            
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

        self._process_state(*args) 

        allowed_transitions = list(filter(lambda dict: dict["from"] == self._state and dict["by"] == "IMMEDIATELY", self._transitions))
        if len(allowed_transitions) == 0: 
            return 

        current_transition = allowed_transitions[0]
        self._state = current_transition["to"]

        self._process_state() 


    def database_ready(self):
        self._process_signal("DB_READY")

    def login(self, username):
        if username: 
            self._process_signal("GUI_LOGIN", username)
    
    def database_auth_ok(self, username):
        self._process_signal("DB_AUTH_OK", username)

    def database_auth_bad(self, error_text):
        self._process_signal("DB_AUTH_BAD", error_text)

    def received_hello(self, name):
        self._process_signal("UR_HELLO", name)

    def received_message(self, message_text, message_type):
        self._process_signal("UR_MESSAGE", message_text, message_type)

    def send_message(self, message_text):
        self._process_signal("GUI_SEND", message_text)

    def change_chat(self, chat_name):
        self._process_signal("GUI_CHAT_CHANGE", chat_name)
