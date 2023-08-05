from enum import Enum


class GenderEnum(str, Enum):
    """Enum representing possible user genders"""
    male = "male"
    female = "female"


class CollectionEnum(str, Enum):
    """Enum representing different collections in the dataset"""
    people = "people"
    places = "places"
    events = "events"
    dictionaries = "dictionaries"
    systematic_theology = "systematic_theology"
    questions = "questions"


class UserRoles(str, Enum):
    """Enum representing possible user roles"""
    basic = "basic"
    translator = "translator"
    editor = "editor"
    admin = "admin"


class UserStatus(str, Enum):
    """Enum represents the status of the user
    The user's account is in good standing and they can access the system or service.
    The user's account is temporarily disabled. They cannot access the system or service until their account is reactivated.
    The user's account has been suspended, usually due to a policy violation. Reinstatement typically requires administrative action.
    The account has been deleted. This is usually irreversible, and the user would need to create a new account to use the service again.
    The user has created an account but has not yet completed the necessary steps to activate it, such as email verification.
    The user's account has been locked due to multiple failed login attempts. The account can typically be unlocked by resetting the password or after a certain period of time."""
    Active = "active"
    Inactive = "Inactive"
    Suspended = "Suspended"
    Deleted = "deleted"
    Pending = "pending"
    Locked = "locked"
