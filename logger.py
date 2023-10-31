import sys


class Logger:
    ERROR = 0
    WARNING = 1
    INFO = 2
    DEBUG = 3
    TRACE = 4
    names = ["[E]", "[W]", "[I]", "[D]", "[T]"]
    COLOR = {
        ERROR: "\033[31m",
        WARNING: "\033[33m",
        INFO: "\033[32m",
        DEBUG: "\033[37m",
        TRACE: "\033[35m"
    }
    ENDCOLOR = "\033[0m"
    
    def __new__(cls, log_level, stdout=True, file=None):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
            cls.instance.__init__(log_level, stdout, file)
        return cls.instance
    
    def __init__(self, log_level, stdout=True, file=None):
        self.log_level = log_level
        self.stdout = stdout
        self.file = file
        
    def log(self, log_level, *args, **kwargs):
        if log_level <= self.log_level:
            message = ' '.join(map(str, args))
            formatted_message = f"[{log_level}] {message}"
            if self.stdout:
                color = self.COLOR.get(log_level, '')
                end_color = self.ENDCOLOR if color else ''
                print(f"{color}{formatted_message}{end_color}", **kwargs)
            if self.file:
                with open(self.file, 'a') as f:
                    f.write(formatted_message + '\n')
                    
    def set_log_levels(self, log_level):
        if log_level in range(len(Logger.names)):
            self.log_level = log_level
            
    def e(self, *args, **kwargs):
        self.log(self.ERROR, *args, **kwargs)
        
    def i(self, *args, **kwargs):
        self.log(self.INFO, *args, **kwargs)
        
    def w(self, *args, **kwargs):
        self.log(self.WARNING, *args, **kwargs)
        
    def d(self, *args, **kwargs):
        self.log(self.DEBUG, *args, **kwargs)
        
    def t(self, *args, **kwargs):
        self.log(self.TRACE, *args, **kwargs)

log = Logger(Logger.DEBUG)