from faker import Faker

__fake = Faker()

correct_random_generate_full_body = {
  "id": __fake.random.randint(1, 1000),
  "username": __fake.user_name(),
  "firstName": __fake.unique.first_name(),
  "lastName": __fake.unique.last_name(),
  "email": __fake.email(),
  "password": __fake.password(),
  "phone": __fake.phone_number(),
  "userStatus": __fake.random.randint(-1000, 1000)
}

without_username_random_generate_full_body = {
  "id": __fake.random.randint(1, 1000),
  "firstName": __fake.unique.first_name(),
  "lastName": __fake.unique.last_name(),
  "email": __fake.email(),
  "password": __fake.password(),
  "phone": __fake.phone_number(),
  "userStatus": __fake.random.randint(-1000, 1000)
}

without_firstName_random_generate_full_body = {
  "id": __fake.random.randint(1, 1000),
  "username": __fake.user_name(),
  "lastName": __fake.unique.last_name(),
  "email": __fake.email(),
  "password": __fake.password(),
  "phone": __fake.phone_number(),
  "userStatus": __fake.random.randint(-1000, 1000)
}

without_lastName_random_generate_full_body = {
  "id": __fake.random.randint(1, 1000),
  "username": __fake.user_name(),
  "firstName": __fake.unique.first_name(),
  "email": __fake.email(),
  "password": __fake.password(),
  "phone": __fake.phone_number(),
  "userStatus": __fake.random.randint(-1000, 1000)
}

without_email_random_generate_full_body = {
  "id": __fake.random.randint(1, 1000),
  "username": __fake.user_name(),
  "firstName": __fake.unique.first_name(),
  "lastName": __fake.unique.last_name(),
  "password": __fake.password(),
  "phone": __fake.phone_number(),
  "userStatus": __fake.random.randint(-1000, 1000)
}

without_password_random_generate_full_body = {
  "id": __fake.random.randint(1, 1000),
  "username": __fake.user_name(),
  "firstName": __fake.unique.first_name(),
  "lastName": __fake.unique.last_name(),
  "email": __fake.email(),
  "phone": __fake.phone_number(),
  "userStatus": __fake.random.randint(-1000, 1000)
}

without_phone_random_generate_full_body = {
  "id": __fake.random.randint(1, 1000),
  "username": __fake.user_name(),
  "firstName": __fake.unique.first_name(),
  "lastName": __fake.unique.last_name(),
  "email": __fake.email(),
  "password": __fake.password(),
  "userStatus": __fake.random.randint(-1000, 1000)
}

without_userStatus_random_generate_full_body = {
  "id": __fake.random.randint(1, 1000),
  "username": __fake.user_name(),
  "firstName": __fake.unique.first_name(),
  "lastName": __fake.unique.last_name(),
  "email": __fake.email(),
  "password": __fake.password(),
  "phone": __fake.phone_number(),
}

empty_body = {}

negative_id_random_generate_full_body = {
  "id": __fake.random.randint(-1000, 0),
  "username": __fake.user_name(),
  "firstName": __fake.unique.first_name(),
  "lastName": __fake.unique.last_name(),
  "email": __fake.email(),
  "password": __fake.password(),
  "phone": __fake.phone_number(),
}
