class UserExampleData:
    user_base = {
        "email": "myemail@domain.com",
        "firstName": "John",
        "lastName": "Doe",
        "gender": "male",
        "birthdate": "1980-05-28"
    }
    user = {**user_base, "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
            "password": "password", "role": "basic", "status": "pending"}
    user_registeration = {**user_base, "password": "password"}
    user_response = {
        "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e", **user_base, "role": "basic"}
    user_log_in = {"email": "myemail@domain.com", "password": "password"}
