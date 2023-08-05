import time
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from config import settings
from features.security.token_model import Token
from bson import ObjectId


SERVER_KEY = settings.secret_key
ALGORITHM = settings.algorithm


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth")

# encode token function


def generate_token(email: str):
    expiration = time.time() + settings.expiration_minutes * 60
    payload = {"email": email,
               "expiration": expiration}
    encoded_jwt = jwt.encode(payload, SERVER_KEY, algorithm=ALGORITHM)
    return Token(access_token=encoded_jwt, token_type="bearer")


def generate_validation_token(email: str, random_text: str, minutes: int = 43200):
    expiration = time.time() + minutes * 60
    payload = {"email": email,
               "token": random_text, "expiration": expiration}
    encoded_jwt = jwt.encode(payload, SERVER_KEY, algorithm=ALGORITHM)
    return Token(access_token=encoded_jwt, token_type="bearer")


def generate_access_token(_id: str, email: str, status: str, role: str):
    if isinstance(_id, ObjectId):
        _id = str(_id)
    expiration = time.time() + 360 * 60
    payload = {"email": email,
               "_id": _id,
               "status": status,
               "role": role,
               "expiration": expiration}
    encoded_jwt = jwt.encode(payload, SERVER_KEY, algorithm=ALGORITHM)
    return Token(access_token=encoded_jwt, token_type="bearer")


# decode access_token function


def decode_access_token(provided_token: str = Depends(oauth2_scheme)):
    try:
        # print(provided_token)
        # print('start_decpde_access')
        payload = jwt.decode(provided_token, SERVER_KEY,
                             algorithms=[ALGORITHM])
        # print(payload)
        decoded_id: str = payload.get("_id")
        # print(decoded_id)
        decoded_time: str = payload.get("expiration")
        if decoded_time < time.time():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The token is expired.",
                headers={"WWW-Authenticate": "Bearer"}
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return decoded_id


# decode token function


def decode_token_id(provided_token: str = Depends(oauth2_scheme)):
    try:
        print(provided_token)
        payload = jwt.decode(provided_token, SERVER_KEY,
                             algorithms=[ALGORITHM])
        # print(payload)
        decoded_id: str = payload.get("user_id")
        decoded_time: str = payload.get("expiration")
        if decoded_time < time.time():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The token is expired.",
                headers={"WWW-Authenticate": "Bearer"}
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return decoded_id


def decode_token_email(provided_token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(provided_token, SERVER_KEY,
                             algorithms=[ALGORITHM])
        decoded_email: str = payload.get("email")
        decoded_time: str = payload.get("expiration")
        if decoded_time < time.time():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The token is expired.",
                headers={"WWW-Authenticate": "Bearer"}
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return decoded_email


def decode_token_status(provided_token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(provided_token, SERVER_KEY,
                             algorithms=[ALGORITHM])
        decoded_status: str = payload.get("status")
        decoded_time: str = payload.get("expiration")
        if decoded_time < time.time():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The token is expired.",
                headers={"WWW-Authenticate": "Bearer"}
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return decoded_status

def decode_token_role(provided_token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(provided_token, SERVER_KEY,
                             algorithms=[ALGORITHM])
        decoded_role: str = payload.get("role")
        decoded_time: str = payload.get("expiration")
        if decoded_time < time.time():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The token is expired.",
                headers={"WWW-Authenticate": "Bearer"}
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return decoded_role


##### decode email for validation #####
def decode_token_email_validation(provided_token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(provided_token, SERVER_KEY,
                             algorithms=[ALGORITHM])
        decoded_email: str = payload.get("email")
        decoded_time: str = payload.get("expiration")
        if decoded_time < time.time():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The Token was expired",
                headers={"WWW-Authenticate": "Bearer"}
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="The token is invalid. please use the sent link without modification."
        )
    return decoded_email

# decode the randome key that is generated.


def decode_token_string(provided_token: str = Depends(oauth2_scheme)):
    """return the random string which is added."""
    try:
        payload = jwt.decode(provided_token, SERVER_KEY,
                             algorithms=[ALGORITHM])
        decoded_status: str = payload.get("token")
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return decoded_status
