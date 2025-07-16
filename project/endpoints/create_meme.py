import requests
import allure
from project.endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    id = None

    @allure.step('Create new meme')
    def create_meme(self, body, token):
        #headers = headers if headers else self.headers
        self.headers['Authorization'] = token
        self.response = requests.post(
            self.url,
            json=body,
            headers=self.headers
        )
        try:
            self.response_json = self.response.json()
            self.id = self.response_json['id']
            return self.response
        except ValueError:
            return self.response

