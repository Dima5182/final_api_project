import requests
import allure
from project.endpoints.endpoint import Endpoint


class GetOneMeme(Endpoint):
    id = None
    token = None

    @allure.step('Get one meme')
    def get_one_meme(self, id, token):
        #headers = headers if headers else self.headers
        self.headers['Authorization'] = token
        self.response = requests.get(
            f'{self.url}/{id}',
            headers=self.headers
        )
        #self.response_json = self.response.json()
        return self.response
