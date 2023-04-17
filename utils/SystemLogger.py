from metaclasses.Singleton import SingletonMetaClass
from pathlib import Path
from loguru import logger
from utils.ConfigData import ConfigData
import datetime
import os


class SystemLogger(metaclass=SingletonMetaClass):
    __LOG_PATH_DIR = Path(Path().cwd(),
                          ConfigData().get_from_log_config('logsDir'))

    __CURRENT_DATE_DIR = Path(Path().cwd(),
                              ConfigData().get_from_log_config('logsDir'),
                              str(datetime.datetime.now().date()))
    __LOG_PATH_JOURNAL = Path(Path().cwd(),
                              ConfigData().get_from_log_config('logsDir'),
                              str(datetime.datetime.now().date()),
                              str(datetime.datetime.now().time().strftime('%H:%M:%S')) + '.log')
    __LOGGER = logger

    def __init__(self):
        self.__create_log_dir()
        self.__create_current_date_dir()
        logger.add(self.__LOG_PATH_JOURNAL,
                   format=ConfigData().get_from_log_config('format'))

    def __create_log_dir(self):
        if not os.path.exists(self.__LOG_PATH_DIR):
            os.mkdir(self.__LOG_PATH_DIR)

    def __create_current_date_dir(self):
        if os.path.exists(self.__CURRENT_DATE_DIR):
            self.__clear_logs_journal()
        else:
            os.mkdir(self.__CURRENT_DATE_DIR)
            self.__clear_logs_journal()

    def __clear_logs_journal(self):
        file = open(self.__LOG_PATH_JOURNAL, 'w')
        file.close()

    def print_warning(self, message):
        self.__LOGGER.warning(message)

    def print_error(self, message):
        self.__LOGGER.error(message)

    def print_debug(self, message):
        self.__LOGGER.debug(message)

    def print_info(self, message):
        self.__LOGGER.info(message)
