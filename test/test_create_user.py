from api.PetsApi import PetsApi
from test_data import create_user_method_data
from schemas import correct_create_user_schema
import pytest

api = PetsApi()

test_data = [
    (200, create_user_method_data.correct_random_generate_full_body, 200, 'unknown'),
    (200, create_user_method_data.without_username_random_generate_full_body, 200, 'unknown'),
    (200, create_user_method_data.without_firstName_random_generate_full_body, 200, 'unknown'),
    (200, create_user_method_data.without_lastName_random_generate_full_body, 200, 'unknown'),
    (200, create_user_method_data.without_email_random_generate_full_body, 200, 'unknown'),
    (200, create_user_method_data.without_password_random_generate_full_body, 200, 'unknown'),
    (200, create_user_method_data.without_phone_random_generate_full_body, 200, 'unknown'),
    (200, create_user_method_data.without_userStatus_random_generate_full_body, 200, 'unknown')
]


@pytest.mark.parametrize('status_code,body,resp_code,resp_type', test_data)
def test_creating_correct_user(status_code: int, body: dict, resp_code: int, resp_type: str):
    response = api.create_user(body,
                               correct_create_user_schema.valid_schema)
    assert response.status == status_code, "Incorrect status code"
    assert response.body['code'] == resp_code, "Incorrect code in response body"
    assert response.body['type'] == resp_type, "Incorrect type in response body"
    assert response.body['message'] == str(body['id']), "Incorrect message in response body"


def test_creating_empty_user():
    response = api.create_user(create_user_method_data.empty_body, correct_create_user_schema.valid_schema)
    assert response.status == 200, "Incorrect status code"
    assert response.body['code'] == 200, "Incorrect code in response body"
    assert response.body['type'] == 'unknown', "Incorrect type in response body"
    assert response.body['message'] == '0', "Incorrect message in response body"


def test_creating_user_with_zero_or_lower_id():
    response = api.create_user(create_user_method_data.negative_id_random_generate_full_body,
                               correct_create_user_schema.valid_schema)
    assert response.status == 200, "Incorrect status code"
    assert response.body['code'] == 200, "Incorrect code in response body"
    assert response.body['type'] == 'unknown', "Incorrect type in response body"
    assert response.body['message'] != '0' and \
           response.body['message'] != str(create_user_method_data.negative_id_random_generate_full_body['id']), \
           "Incorrect message in response body"
