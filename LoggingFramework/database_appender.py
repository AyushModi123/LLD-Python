from log_appender import LogAppender
from log_message import LogMessage
from log_level import LogLevel
import os

class DatabaseAppender(LogAppender):

    def append(self, msg: str):
        print("Database Appended: ", msg)
            
        