from file_appender import FileAppender
from log_level import LogLevel

from logger import Logger

logger = Logger()
logger.debug("DEBUGGING")
logger.error("ERROR")
logger.log("HEY")

print(logger.get_log_level())
print(logger.get_log_appender())

logger.set_log_level(LogLevel.ERROR)
logger.set_log_appender(FileAppender("LoggingFramework/log.txt"))

print(logger.get_log_level())
print(logger.get_log_appender())

logger.log("ERROR!")

logger.set_file_path("temp/log.txt")

logger.error("ERROR")