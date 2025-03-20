import requests
class DataAPI:
    def __init__(self, api_token: str):
        self.base_url = "https://api.TEST-SERVER/v1"
        self.headers = {"Authorization": api_token}
        print('---====Data API initialized with TEST Values. Need to set real values. ====---')

    def __get_data(self, url, params=None):
        return requests.get(url, headers=self.headers, params=params).json()

    def get_file(self, file_name: str):
        print('Data API try to get file')
        return self.__get_data(
            f"{self.base_url}/datasets/files/{file_name}"
        )