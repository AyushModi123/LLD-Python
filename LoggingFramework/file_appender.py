from log_appender import LogAppender
from log_message import LogMessage
from log_level import LogLevel
import os

class FileAppender(LogAppender):
    def __init__(self, filepath: str) -> None:
        if not os.path.exists(filepath):            
            directory = os.path.dirname(filepath)
            if not os.path.exists(directory):
                os.makedirs(directory)
            open(filepath, 'a').close()
        self._filepath = filepath

    def append(self, msg: str):
        with open(self._filepath, 'a') as f:
            f.write(msg + '\n')
        