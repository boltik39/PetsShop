import configparser
from metaclasses.Singleton import SingletonMetaClass
from pathlib import Path


class SecretData(metaclass=SingletonMetaClass):
    __READY_CONFIG = None
    __SECRET_PATH = Path(Path().cwd(), 'secrets', 'secrets.ini')

    def __init__(self):
        self.__ready_data()

    def __ready_data(self):
        self.ready_secret = configparser.ConfigParser()
        self.ready_secret.read(self.__SECRET_PATH)

    def get_from_secrets(self, param):
        return self.ready_secret["Secrets"][param]
