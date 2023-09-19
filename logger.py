import sys


class Logger:
    ERROR = 0
    WARNING = 1
    INFO = 2
    DEBUG = 3
    TRACE = 4
    names = ("[E] ", "[W] ", "[I] ", "[D] ", "[T] ")

    def __new__(cls, *args):
        if not hasattr(cls, 'Instance'):
            cls.Instance = super(Logger, cls).__new__(cls)
        return cls.Instance

    def __init__(self, level, stdout=True, file=None):
        self.level = level
        self.stdout = stdout
        self.file = file

    def _log(self, level, *args, **kwargs):
        if level >= len(Logger.names):
            return
        if level > self.level:
            return
        if self.stdout is False:
            return (Logger.names[level], args, kwargs)
        if self.file:
            return self._log_file(level, *args, **kwargs)
        print(f'\033[32m{Logger.names[level]}\033[0m', *args, **kwargs)

    def _log_file(self, level, *args, **kwargs):
        log_file = open(f'{self.file}', 'a', encoding='utf-8')
        stdout_save = sys.stdout
        sys.stdout = log_file
        print(Logger.names[level], *args, **kwargs)
        log_file.close()
        sys.stdout = stdout_save

    def set(self, level=None):
        if level is None:
            return self.level
        self.level = level
        return self.level

    def e(self, *args, **kwargs):
        self._log(Logger.ERROR, *args, **kwargs)

    def w(self, *args, **kwargs):
        self._log(Logger.WARNING, *args, **kwargs)

    def i(self, *args, **kwargs):
        self._log(Logger.INFO, *args, **kwargs)

    def d(self, *args, **kwargs):
        self._log(Logger.DEBUG, *args, **kwargs)

    def t(self, *args, **kwargs):
        self._log(Logger.TRACE, *args, **kwargs)