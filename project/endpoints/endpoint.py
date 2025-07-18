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
        assert self.response.json()['text'] == text

    @allure.step('Check that tags are the same as sent')
    def check_response_tags_are_correct(self, tags):
        assert self.response.json()['tags'] == tags

    @allure.step('Check that info is the same as sent')
    def check_response_info_is_correct(self, info):
        assert self.response.json()['info'] == info

    @allure.step('Check that url is the same as sent')
    def check_response_url_is_correct(self, url):
        assert self.response.json()['url'] == url

    @allure.step('Check that id is the same as sent')
    def check_response_id_is_correct(self, object_id):
        assert self.response.json()['id'] == object_id

    @allure.step('Check that response is not empty')
    def check_response_json_is_not_empty(self):
        assert len(self.response.json()) > 0
