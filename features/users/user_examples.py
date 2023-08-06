class UserExampleData:
    user_base = {
        "email": "myemail@domain.com",
        "firstName": "John",
        "lastName": "Doe",
        "gender": "male",
        "birthdate": "1980-05-28"
    }
    user = {**user_base, "_id": "64cfb0a0f63ee5eacc93dac3",
            "password": "password", "role": "basic", "status": "pending"}
    user_registeration = {**user_base, "password": "password"}
    user_response = {
        "_id": "64cfb0a0f63ee5eacc93dac3", **user_base, "role": "basic", "status": "pending"}
    user_log_in = {"email": "myemail@domain.com", "password": "password"}
    user_role_update = {
        "_id": "64cfb0a0f63ee5eacc93dac3", "role": "translator"}
