import pytest

def test_get_all_meme(get_all_meme_endpoint, get_token_endpoint):
    get_all_meme_endpoint.get_all_meme(get_token_endpoint.get_token())
    get_all_meme_endpoint.check_response_status_code_is_200()

def test_get_all_meme_unauthorized(get_all_meme_endpoint):
    get_all_meme_endpoint.get_all_meme("invalid_token")
    get_all_meme_endpoint.check_response_status_code_is_401()

TEST_DATA_CREATE = [{"text": "teststring",
    "url": "https://jrnlst.ru/wp-content/uploads/2023/03/cover_6-1024x644.jpg",
    "tags": ["tag1", "tag2"],
    "info": {"color": "test_color"}},
    {"text": "teststring2",
    "url": "https://jrnlst.ru/wp-content/uploads/2023/03/cover_6-1024x644.jpg",
    "tags": ["tag1", "tag3"],
    "info": {"color": "test_color2"}}]

@pytest.mark.parametrize('data', TEST_DATA_CREATE)
def test_create_meme(create_meme_endpoint, get_token_endpoint, data):
    create_meme_endpoint.create_meme(token=get_token_endpoint.get_token(), body=data)
    create_meme_endpoint.check_response_status_code_is_200()

@pytest.mark.parametrize('data', TEST_DATA_CREATE)
def test_create_meme_unauthorized(create_meme_endpoint, data):
    create_meme_endpoint.create_meme(token="badtoken", body=data)
    create_meme_endpoint.check_response_status_code_is_401()

@pytest.mark.parametrize("invalid_data", [
    {},
    {"text": "meme"},
    {"url": "https://example.com"},
    {"tags": ["tag1", "tag3"]},
    {"info": {"color": "test_color2"}},
    {"text": 123, "url": "https://example.com", "tags": ["tag1", "tag3"], "info": {"color": "test_color2"}},
    {"text": "meme", "url": {}, "tags": ["tag1", "tag3"], "info": {"color": "test_color2"}},
    {"text": "meme", "url": "https://example.com", "tags": "tag1", "info": {"color": "test_color2"}},
    {"text": "123", "url": "https://example.com", "tags": ["tag1", "tag3"], "info": "test_color2"},
    {"text": "123", "url": "https://example.com", "tags": ["tag1", "tag3"]},
    {"text": "123", "url": "https://example.com", "info": {"color": "test_color2"}},
    {"text": "123", "tags": ["tag1", "tag3"], "info": {"color": "test_color2"}},
    {"url": "https://example.com", "tags": ["tag1", "tag3"], "info": {"color": "test_color2"}}
])
def test_create_invalid_meme(create_meme_endpoint, get_token_endpoint, invalid_data):
    create_meme_endpoint.create_meme(token=get_token_endpoint.get_token(), body=invalid_data)
    create_meme_endpoint.check_response_status_code_is_400()

def test_get_one_meme(get_one_meme_endpoint, get_token_endpoint, object_id):
    get_one_meme_endpoint.get_one_meme(object_id, get_token_endpoint.get_token())
    get_one_meme_endpoint.check_response_status_code_is_200()

@pytest.mark.parametrize("invalid_id", ['abc', -1, 0, 9999999])
def test_get_one_invalid(get_one_meme_endpoint, get_token_endpoint, invalid_id):
    get_one_meme_endpoint.get_one_meme(id=invalid_id, token=get_token_endpoint.get_token())
    get_one_meme_endpoint.check_response_status_code_is_404()

def test_delete_meme(delete_meme_endpoint, get_token_endpoint, object_id):
    delete_meme_endpoint.delete_meme(object_id, get_token_endpoint.get_token())
    delete_meme_endpoint.check_response_status_code_is_200()

def test_delete_meme_another_user(delete_meme_endpoint, get_token_endpoint, object_id):
    another_user_token = get_token_endpoint.get_token('False Iron man')
    delete_meme_endpoint.delete_meme(object_id, another_user_token)
    delete_meme_endpoint.check_response_status_code_is_403()

def test_delete_meme_unauthorized(delete_meme_endpoint, object_id):
    delete_meme_endpoint.delete_meme(object_id, token="invalidtoken")
    delete_meme_endpoint.check_response_status_code_is_401()

@pytest.mark.parametrize("invalid_id", ["abc", -1, 0, 999999])
def test_delete_meme_with_invalid_id(delete_meme_endpoint, get_token_endpoint, invalid_id):
    delete_meme_endpoint.delete_meme(id=invalid_id, token=get_token_endpoint.get_token())
    delete_meme_endpoint.check_response_status_code_is_404()

TEST_DATA_PUT = [{
"text": "teststring3",
"url": "https://jrnlst.ru/wp-content/uploads/2023/03/cover_6-1024x644.jpg",
"tags": ["tag33", "tag44"],
"info": {"color": "test_color3"}},
                 {
                  "text": "teststring4",
                  "url": "https://jrnlst.ru/wp-content/uploads/2023/03/cover_6-1024x644.jpg",
                  "tags": ["tag44", "tag55"],
                  "info": {"color": "test_color4"}}]

@pytest.mark.parametrize('data', TEST_DATA_PUT)
def test_put_meme(change_meme_endpoint, get_token_endpoint, object_id, data):
    change_meme_endpoint.change_meme(id=object_id, body=data, token=get_token_endpoint.get_token())
    change_meme_endpoint.check_response_status_code_is_200()
    change_meme_endpoint.check_response_text_is_correct(data['text'])

@pytest.mark.parametrize('data', TEST_DATA_PUT)
def test_put_meme_another_user(change_meme_endpoint, get_token_endpoint, object_id, data):
    change_meme_endpoint.change_meme(id=object_id, body=data, token=get_token_endpoint.get_token('False Iron man'))
    change_meme_endpoint.check_response_status_code_is_403()

TEST_DATA_INCORRECT_PUT = [
    {},
    {"text": "meme"},
    {"url": "https://example.com"},
    {"tags": ["tag1", "tag3"]},
    {"info": {"color": "test_color2"}},
    {"text": 123, "url": "https://example.com", "tags": ["tag1", "tag3"], "info": {"color": "test_color2"}},
    {"text": "meme", "url": {}, "tags": ["tag1", "tag3"], "info": {"color": "test_color2"}},
    {"text": "meme", "url": "https://example.com", "tags": "tag1", "info": {"color": "test_color2"}},
    {"text": "123", "url": "https://example.com", "tags": ["tag1", "tag3"], "info": "test_color2"},
    {"text": "123", "url": "https://example.com", "tags": ["tag1", "tag3"]},
    {"text": "123", "url": "https://example.com", "info": {"color": "test_color2"}},
    {"text": "123", "tags": ["tag1", "tag3"], "info": {"color": "test_color2"}},
    {"url": "https://example.com", "tags": ["tag1", "tag3"], "info": {"color": "test_color2"}}
]
@pytest.mark.parametrize('data', TEST_DATA_INCORRECT_PUT)
def test_update_meme_with_invalid_data(change_meme_endpoint, get_token_endpoint, object_id, data):
    change_meme_endpoint.change_meme(id=object_id, body=data, token=get_token_endpoint.get_token())
    change_meme_endpoint.check_response_status_code_is_400()

@pytest.mark.parametrize("invalid_id", ["abc", -1, 0, 999999])
def test_update_meme_with_invalid_id(change_meme_endpoint, get_token_endpoint, invalid_id):
    change_meme_endpoint.change_meme(id=invalid_id, body={
"text": "teststring3",
"url": "https://jrnlst.ru/wp-content/uploads/2023/03/cover_6-1024x644.jpg",
"tags": ["tag33", "tag44"],
"info": {"color": "test_color3"}}, token=get_token_endpoint.get_token())
    change_meme_endpoint.check_response_status_code_is_404()
