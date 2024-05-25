from log_appender import LogAppender
from log_message import LogMessage
from log_level import LogLevel
import os

class FileAppender(LogAppender):
    def __init__(self, filepath: str) -> None:
        self._make_dirs(filepath)
        self._filepath = filepath

    def append(self, msg: str):
        with open(self._filepath, 'a') as f:
            f.write(msg + '\n')

    def get_file_path(self):
        return self._filepath

    def set_filepath(self, filepath: str) -> None:
        self._make_dirs(filepath)
        self._filepath = filepath
        
    def _make_dirs(self, filepath: str):
        if not os.path.exists(filepath):            
            directory = os.path.dirname(filepath)
            if not os.path.exists(directory):
                os.makedirs(directory)
            open(filepath, 'a').close()