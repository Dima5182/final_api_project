import allure
import requests


class Endpoint:
    url = 'http://167.172.172.115:52355/meme'
    response = None
    response_json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that status code is 200')
    def check_response_status_code_is_200(self):
        assert self.response.status_code == 200, 'Status code is not 200'

    @allure.step('Check that status code is 401')
    def check_response_status_code_is_401(self):
        assert self.response.status_code == 401, 'Status code is not 401'

    @allure.step('Check that status code is 404')
    def check_response_status_code_is_404(self):
        assert self.response.status_code == 404, 'Status code is not 404'

    @allure.step('Check that status code is 400')
    def check_response_status_code_is_400(self):
        assert self.response.status_code == 400, 'Status code is not 400'

    @allure.step('Check that status code is 403')
    def check_response_status_code_is_403(self):
        assert self.response.status_code == 403, 'Status code is not 403'

    @allure.step('Check that text is the same as sent')
    def check_response_text_is_correct(self, text):
        assert self.response_json['text'] == text

    @allure.step('Check that id is the same as sent')
    def check_response_id_is_correct(self, object_id):
        assert self.response_json['id'] == object_id
