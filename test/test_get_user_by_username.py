import pytest

from api.PetsApi import PetsApi
from schemas import successful_get_user_by_username_schema
from schemas import unsuccessful_request_schema
from test_data import get_user_by_username_data
from schemas import correct_create_user_schema

test_data = [
    (get_user_by_username_data.correct_user_body, 200, 200),
    (get_user_by_username_data.not_full_user_body, 200, 200)
]
api = PetsApi()


@pytest.mark.parametrize('create_user_body,create_user_status,get_user_status', test_data)
def test_get_correct_user_by_username(create_user_body: dict, create_user_status: int, get_user_status: int):
    create_user_response = api.create_user(create_user_body,
                                           correct_create_user_schema.valid_schema)
    assert create_user_response.status == create_user_status
    get_user_response = api.get_user_by_username(create_user_body['username'],
                                                 successful_get_user_by_username_schema.valid_schema)
    assert get_user_response.status == get_user_status, "Incorrect status code"
    for key in get_user_response.body:
        assert get_user_response.body[key] == create_user_body[key], "Different keys values"


def test_get_nonexistent_user_by_username():
    get_user_response = api.get_user_by_username(get_user_by_username_data.nonexistent_username,
                                                 unsuccessful_request_schema.valid_schema)
    assert get_user_response.status == get_user_by_username_data.user_not_found_status, "Incorrect status code"
    assert get_user_response.body['code'] == get_user_by_username_data.user_not_found_resp_code, \
        "Incorrect code in response body"
    assert get_user_response.body['type'] == get_user_by_username_data.user_not_found_resp_type, \
        "Incorrect type in response body"
    assert get_user_response.body['message'] == get_user_by_username_data.user_not_found_resp_message, \
        "Incorrect message in response body"
