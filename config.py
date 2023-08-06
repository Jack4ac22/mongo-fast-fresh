from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    algorithm: str
    atlas_uri: str
    db_name: str
    email_address: str
    email_password: str
    expiration_minutes: int
    host_name: str
    secret_key: str

    class Config:
        env_file = ".env"


settings = Settings()
