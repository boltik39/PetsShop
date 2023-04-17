from faker import Faker

__fake = Faker()

correct_user_body = {
  "id": __fake.random.randint(1, 1000),
  "username": __fake.user_name(),
  "firstName": __fake.unique.first_name(),
  "lastName": __fake.unique.last_name(),
  "email": __fake.email(),
  "password": __fake.password(),
  "phone": __fake.phone_number(),
  "userStatus": __fake.random.randint(-1000, 1000)
}

not_full_user_body = {
  "id": __fake.random.randint(1, 1000),
  "username": __fake.user_name(),
  "userStatus": __fake.random.randint(-1000, 1000)
}

nonexistent_username = __fake.unique.user_name()

user_not_found_status = 404
user_not_found_resp_code = 1
user_not_found_resp_type = 'error'
user_not_found_resp_message = 'User not found'
