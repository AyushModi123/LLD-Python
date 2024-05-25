from datetime import datetime
from log_level import LogLevel
from typing import Optional

class LogMessage:        
    
    def __init__(self) -> None:
        self.log_level = LogLevel.INFO

    def create_message(self, msg: str,  log_level: Optional[LogLevel]):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if log_level:
            return f"{self.timestamp} {log_level.name}: {msg}"    
        else:            
            return f"{self.timestamp} {self.log_level.name}: {msg}"
    
    def set_log_level(self, log_level: LogLevel):
        self.log_level = log_level
        
    def get_log_level(self):
        return self.log_level
    