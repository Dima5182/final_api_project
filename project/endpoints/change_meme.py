import requests
import allure
from project.endpoints.endpoint import Endpoint


class ChangeMeme(Endpoint):
    id = None
    token = None

    @allure.step('Update an object')
    def change_meme(self, id, body, token):
        #headers = headers if headers else self.headers
        self.headers['Authorization'] = token
        json_data = {"id": id}
        json_data.update(body)  # добавляет все поля, которые есть

        self.response = requests.put(
            f'{self.url}/{id}',
            json=json_data,
            headers=self.headers
        )
        try:
            self.response_json = self.response.json()
            self.id = self.response_json['id']
            return self.response.status_code
        except ValueError:
            return self.response.status_code
