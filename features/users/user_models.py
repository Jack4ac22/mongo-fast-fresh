from datetime import date, datetime, timedelta
from pydantic import BaseModel, Field, EmailStr, validator, ValidationError
from typing import List, Union
from typing import Optional
import features.users.user_enums as user_enums
import re
import uuid
from features.users.user_examples import UserExampleData


class UserBase(BaseModel):
    """A base model for User, including fields common to all types of User models."""
    # id: str = Field(default_factory=uuid.uuid4, alias="_id")
    email: EmailStr = Field(...)
    firstName: str = Field(...)
    lastName: str = Field(...)
    gender: user_enums.GenderEnum = Field(...)
    birthdate: date = Field(...)
    status: user_enums.UserStatus = Field(default=user_enums.UserStatus.Pending)
    role: user_enums.UserRoles = Field(default=user_enums.UserRoles.basic)

    @validator('birthdate', pre=True)
    def age_must_be_above_16(cls, v):
        try:
            birthdate = datetime.strptime(v, "%Y-%m-%d").date()
        except ValueError:
            raise ValidationError(
                "Invalid date format. Date should be in the format: YYYY-MM-DD")
        if (date.today() - birthdate) < timedelta(days=16*365):
            raise ValidationError('User must be 16 years or older.')
        return birthdate

    @validator('email')
    def validate_email(cls, v):
        # The following regex checks for common email formats
        email_regex = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_regex, v):
            raise ValueError('Invalid email address.')
        return v

    class Config:
        populate_by_name = True


class User(UserBase):
    """The main User model, which includes an id and a password Generally used to register a new user account, not as """
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    password: str = Field(...)
    role: user_enums.UserRoles = Field(
        default_factory=lambda: user_enums.UserRoles.basic)
    status: user_enums.UserStatus

    @validator('password')
    def validate_password(cls, password):
        if len(password) < 8:
            raise ValueError(
                'Password too short, should be at least 8 characters long')
        if not re.search('[A-Z]', password):
            raise ValueError(
                'Password should contain at least one uppercase letter')
        if not re.search('[a-z]', password):
            raise ValueError(
                'Password should contain at least one lowercase letter')
        return password

    class Config(UserBase.Config):
        json_schema_extra = {
            "example": UserExampleData.user_base
        }


class UserRegisteration(UserBase):
    """The main User model, which includes an id and a password-  Generally used to register a new user account."""
    password: str = Field(...)

    class Config(UserBase.Config):
        json_schema_extra = {
            "example": UserExampleData.user_registeration
        }


class UserResponse(UserBase):
    """The main User response model."""
    id: str = Field(..., alias="_id")

    class Config(UserBase.Config):
        json_schema_extra = {
            "example": UserExampleData.user_response
        }


class UserLogIn(BaseModel):
    """A User logining in model."""
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": UserExampleData.user_log_in
        }


class UserRoleUpdate(BaseModel):
    """A User update role body"""
    id: str = Field(..., alias="_id")
    role: user_enums.UserRoles

    class Config:
        populate_by_name = True
        json_schema_extra = {
            'example': UserExampleData.user_role_update
        }
