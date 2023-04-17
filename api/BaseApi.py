from utils.SystemLogger import SystemLogger
import requests


class BaseApi:
    @staticmethod
    def my_req(method: str, url: str, **kwargs) -> requests.Response:
        """
        Custom requests method for future simple library changing
        :param method: each rest methods
        :param url: URL for request
        :param kwargs: other params, e.g. headers, json
        :return: Response object
        """
        try:
            SystemLogger().print_info(f"Send {method} to: {url}")
            response = requests.request(method, url, **kwargs)
            SystemLogger().print_info(f"Status code: {response.status_code}")
            return response
        except requests.exceptions.ConnectionError:
            SystemLogger().print_error(f"Connection error while sending {method} to {url}")
            return requests.Response()
