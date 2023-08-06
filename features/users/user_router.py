from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends, Query
from fastapi.encoders import jsonable_encoder
from features.security.token_model import Token
from features.users import user_db, user_models, user_enums
from features.users.user_models import User, UserRegisteration, UserResponse, UserLogIn
from typing import List, Optional
import time
from utilities import jwt_manager

router = APIRouter()


@router.post("/", response_description="Create a new user", status_code=status.HTTP_201_CREATED, response_model=user_models.UserResponse)
def create_user(request: Request, user: user_models.UserRegisteration = Body(...)):
    user = jsonable_encoder(user)
    return user_db.create_new_user(request, user)


@router.get("/activate", response_description="a confirmation that the users email is activated, providing a token to login.", status_code=status.HTTP_200_OK, response_model=user_models.UserResponse)
def activate_user(request: Request, token: Optional[str] = Query(None)):
    # print('user_router.activate_user.token' + token)
    return user_db.activate_email(request, token)


@router.get('/all', response_description='get all users for admin', status_code=status.HTTP_200_OK, response_model=List[user_models.UserResponse])
def get_all_users(request: Request, user_role: str = Depends(jwt_manager.decode_token_role), user_status: str = Depends(jwt_manager.decode_token_status)):
    return user_db.get_users(request, user_role)


@router.post('/role', response_description='Update user role and return the updated information', status_code=status.HTTP_200_OK, response_model=user_models.UserResponse)
def change_user_role(request: Request, payload: user_models.UserRoleUpdate, user_role: str = Depends(jwt_manager.decode_token_role)):
    response = user_db.change_role(request, payload, user_role)
    return response


@router.get('/{id}', response_description='get user by id', status_code=status.HTTP_200_OK, response_model=user_models.UserResponse)
def get_user_by_id(request: Request, id: str, user_id: str = Depends(jwt_manager.decode_access_token), role: str = Depends(jwt_manager.decode_token_role), status: str = Depends(jwt_manager.decode_token_status)):
    return user_db.find_user(request, id, user_id, role)
