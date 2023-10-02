from PyQt6.QtCore import QObject, pyqtSignal
from logger import log 


class Controller(QObject):
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

    switchWindow = pyqtSignal(str, str)

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
                pass
            case _:
                log.w("Unknown State!")
            
    def _process_signal(self, signal_name, *args):
        allowed_transition = tuple(filter(lambda x: x if x['from'] == self._state
                                                         and x['by'] == signal_name else (), self._transitions))
        if len(allowed_transition) == 0:
            return
        current_transition = allowed_transition[0]
        self._state = current_transition["to"]

        self._process_state(*args)

        allowed_transition = tuple(filter(lambda x: x if x['from'] == self._state
                                                         and x['by'] == 'IMMEDIATELY' else (), self._transitions))
        if len(allowed_transition) == 0:
            return
        current_transition = allowed_transition[0]
        self._state = current_transition["to"]

        self._process_state()

    def database_ready(self):
        self._process_signal('DB_READY')

    def gui_login(self, username):
        if username:
            self._process_signal('GUI_LOGIN', username)

    def database_auth_ok(self):
        self._process_signal('DB_AUTH_OK')

    def database_auth_bad(self):
        self._process_signal('DB_AUTH_BAD')

    def received_hello(self):
        self._process_signal('UR_HELLO')

    def received_message(self, text, type):  # message
        self._process_signal('UR_MESSAGE', text, type)

    def send_message(self):
        self._process_signal('GUI_SEND')

    def change_chat(self):
        self._process_signal('GUI_CHAT_CHANGE')

    def old_login(self, username):
        if username: 
            self.switchWindow.emit("MainWindow", username) 
    
    def old_message_receiver(self, message_text, message_type):
        log.d(f"Сообщение получено '{message_text}' => {message_type}")
