# from db import models
from fastapi import Depends, Response, status, APIRouter, HTTPException, Request
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from utilities import hash_manager, jwt_manager
from features.users import user_functions, user_db

router = APIRouter(
    prefix='/auth',
    tags=['authentication']
)

incorrectException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect username or password ",
    headers={"WWW-Authenticate": "Bearer"}
)


@router.post('', status_code=status.HTTP_202_ACCEPTED)
def auth_user(request: Request, user_credentials: OAuth2PasswordRequestForm = Depends()):

    corresponding_user = user_functions.find_account_by_email(
        request, user_credentials.username)
    # print(corresponding_user)
    if not corresponding_user:
        raise incorrectException

    pass_valid = hash_manager.verify_password(
        user_credentials.password, corresponding_user['password'])

    if not pass_valid:
        raise incorrectException

    jwt = jwt_manager.generate_access_token(
        corresponding_user['_id'], corresponding_user['email'], corresponding_user['status'], corresponding_user['role'], )
    return jwt
