import requests
from project.endpoints.endpoint import Endpoint

class Authorize():
    token = None

    def get_token(self, name='Iron man'):
        body = {"name": name}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'http://167.172.172.115:52355/authorize',
            json=body,
            headers=headers
        )
        self.token = response.json()['token']
        return self.token
