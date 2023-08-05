from datetime import date
from enum import Enum
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
import uuid


class Token(BaseModel):
    access_token: str = "eyJhbGciOiqIUz1NaiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiamFtZSI6IkavaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQasw5c"
    token_type: str = "Bearer"
