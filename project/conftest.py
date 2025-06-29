import pytest
from project.endpoints.get_token import Authorize
from project.endpoints.get_all_meme import GetAllMeme
from project.endpoints.get_one_meme import GetOneMeme
from project.endpoints.create_meme import CreateMeme
from project.endpoints.change_meme import ChangeMeme
from project.endpoints.delete_meme import DeleteMeme

@pytest.fixture()
def get_token_endpoint():
    return Authorize()

@pytest.fixture()
def get_all_meme_endpoint():
    return GetAllMeme()

@pytest.fixture()
def get_one_meme_endpoint():
    return GetOneMeme()

@pytest.fixture()
def create_meme_endpoint():
    return CreateMeme()

@pytest.fixture()
def change_meme_endpoint():
    return ChangeMeme()

@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()

@pytest.fixture()
def object_id(create_meme_endpoint, get_token_endpoint):
    data_for_create = {"text": "teststring",
                       "url": "https://jrnlst.ru/wp-content/uploads/2023/03/cover_6-1024x644.jpg",
                       "tags": ["tag1", "tag2"],
                        "info": {"color": "test_color"}}
    id = create_meme_endpoint.create_meme(body=data_for_create, token=get_token_endpoint.get_token()).json()['id']
    return id
