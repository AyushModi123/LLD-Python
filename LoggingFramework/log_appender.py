from abc import abstractmethod, ABC
from log_message import LogMessage

class LogAppender(ABC):

    @abstractmethod
    def append(msg: LogMessage):
        pass