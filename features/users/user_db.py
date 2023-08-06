from bson import ObjectId
from features.users import user_db, user_functions
from utilities import hash_manager, jwt_manager, email_manager, logger_manager
from config import settings
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from pymongo import MongoClient, errors
from config import settings
from features.users.user_models import User, UserRegisteration, UserResponse, UserLogIn
from features.users import user_enums


def create_new_user(request: Request, user: User):
    """creating a new user based on registeration model. the function will cast the _id to string"""
    # TODO: replace the method with user_functions.find_account_by_email(request, email)
    if request.app.database["users"].find_one({"email": user['email']}):
        user_functions.rais_exeption(
            status.HTTP_400_BAD_REQUEST, "A user with this email already exists.")
    user['password'] = hash_manager.hash_pass(user['password'])
    new_user = request.app.database["users"].insert_one(user)
    created_user = request.app.database["users"].find_one(
        {"_id": new_user.inserted_id})
    email = user['email']
    lastName = user['lastName']
    firstName = user['firstName']
    generated_token = jwt_manager.generate_validation_token(
        email, "ActivateMyAccount", 4320)
    created_user["_id"] = str(created_user["_id"])
    try:
        # email_manager.send_html_validation_email(
        #     email, firstName + ' '+lastName, settings.host_name+'/'+user+"/activate/" + generated_token, 3 )
        email_manager.send_email_with_subject("API registration.", email, "Email Verification link", f"""Hello {firstName} {lastName},
        Please use the following link to verify your account
        {settings.host_name}/user/activate/{generated_token.access_token}
        This token is valid for 24 hrs only.
        Thank you.""")
    except:
        # TODO: add erasing methos, if the email of verification is not sent, we delete the user and ask him to try again later.
        # db["users"].delete_one({"_id": new_user.inserted_id})
        print("exception")
    return created_user


def activate_email(request: Request, token: str):
    # print('user_db.activate_email.token'+token)
    email = jwt_manager.decode_token_email_validation(token)
    # print('user_db.activate_email.email'+ email)
    text = jwt_manager.decode_token_string(token)
    # print('user_db.activate_email.text'+text)
    if text == "ActivateMyAccount":
        user = user_functions.avtivate_account(request, email)
        user["_id"] = str(user["_id"])
        return user
# TODO: add login token as return


def find_user(request: Request, id: str, user_id: str, role: str):
    """
    finding user in the data base based on the id and the user id which is provided in the token where a logic will be applied to validate the request.
    """
# check the status and id
    # print(id)
    # print(user_id)
    # print(role)
    if ((id == user_id) or (role == user_enums.UserRoles.admin)):
        try:
            object_id = ObjectId(id)
            retrieved_user = request.app.database["users"].find_one(
                {"_id": object_id})
            if isinstance(retrieved_user['_id'], ObjectId):
                str_id = str(retrieved_user['_id'])
                retrieved_user['_id'] = str_id
            # print(retrieved_user)
            if retrieved_user is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found",
                )
            return retrieved_user

        except Exception as e:
            print("Error:", e)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid id format or database error",
            )
    else:
        user_functions.rais_exeption(status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                                     "The requested information exceeds your security level")


def get_users(request: Request, user_status: str):
    print('user_status: ' + user_status)
    print(user_enums.UserRoles.admin)
    if user_status == user_enums.UserRoles.admin:
        try:
            users = list(request.app.database["users"].find(limit=100))
            for user in users:
                if isinstance(user['_id'], ObjectId):
                    str_id = str(user['_id'])
                    user['_id'] = str_id
            return users
        except:
            pass
    else:
        user_functions.rais_exeption(status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                                     "The requested information exceeds your security level")
