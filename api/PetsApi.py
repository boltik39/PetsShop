from metaclasses.Singleton import SingletonMetaClass
from utils.ConfigData import ConfigData
from utils.SecretData import SecretData
from jsonschema import validate
from api.BaseApi import BaseApi
from models.ResponseModel import ResponseModel


class PetsApi(metaclass=SingletonMetaClass):
    __TOKEN = SecretData().get_from_secrets('token')
    __BASE_URL = ConfigData().get_from_pets_api_config('base_url')
    __AUTH_TYPE = ConfigData().get_from_pets_api_config('auth_type')

    __CREATE_USER_METHOD = ConfigData().get_from_pets_api_config('create_user')
    __GET_USER_BY_USERNAME_METHOD = ConfigData().get_from_pets_api_config('get_user_by_username')

    __HEADERS = {
        "Authorization": f"{__AUTH_TYPE} {__TOKEN}"
    }

    def get_user_by_username(self, username: str, schema: dict):
        response = BaseApi.my_req("GET", self.__BASE_URL + self.__GET_USER_BY_USERNAME_METHOD + username,
                                  headers=self.__HEADERS)
        validate(instance=response.json(), schema=schema)
        return ResponseModel(status=response.status_code, body=response.json())

    def create_user(self, body: dict, schema: dict):
        response = BaseApi.my_req("POST", self.__BASE_URL + self.__CREATE_USER_METHOD, headers=self.__HEADERS,
                                  json=body)
        validate(instance=response.json(), schema=schema)
        return ResponseModel(status=response.status_code, body=response.json())
