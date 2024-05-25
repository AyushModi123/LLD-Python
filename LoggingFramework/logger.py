from log_level import LogLevel
from log_appender import LogAppender
from log_message import LogMessage
from console_appender import ConsoleAppender

class Logger:
    _instance = None
    _log_message = LogMessage()
    _log_appender = ConsoleAppender()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)            
        return cls._instance

    def log(self, msg: str):
        self._log_appender.append(self._log_message.create_message(msg, self._log_message.get_log_level()))

    def set_log_appender(self, log_appender: LogAppender):
        self._log_appender = log_appender

    def get_log_appender(self):
        return self._log_appender
    
    def set_log_level(self, log_level: LogLevel):
        self._log_message.set_log_level(log_level)

    def get_log_level(self):
        return self._log_message.get_log_level()
    
    def debug(self, msg: str):
        self._log_appender.append(self._log_message.create_message(msg, LogLevel.DEBUG))

    def info(self, msg: str):
        self._log_appender.append(self._log_message.create_message(msg, LogLevel.INFO))

    def error(self, msg: str):
        self._log_appender.append(self._log_message.create_message(msg, LogLevel.ERROR))
    
    def fatal(self, msg: str):
        self._log_appender.append(self._log_message.create_message(msg, LogLevel.FATAL))
    
    def warning(self, msg: str):
        self._log_appender.append(self._log_message.create_message(msg, LogLevel.WARNING))
    


    

        