from pydantic import BaseModel


class UserData(BaseModel):
    first_name: str
    last_name: str
    username: str
    birthdate: str
    time_left: str
