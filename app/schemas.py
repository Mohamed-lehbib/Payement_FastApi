# schemas.py
import re
from pydantic import BaseModel, constr, validator

class ClientBase(BaseModel):
    id_number: constr(min_length=10, max_length=10)
    first_name: str
    last_name: str

class AccountBase(BaseModel):
    account_number: constr(min_length=16, max_length=16)
    balance: float
    owner_id: constr(min_length=10, max_length=10)

class CardBase(BaseModel):
    card_number: constr(min_length=16, max_length=16)
    owner: str
    cvv: constr(min_length=3, max_length=3)
    expiration_date: constr(min_length=5, max_length=5)
    balance: float

    @validator('expiration_date')
    def validate_expiration_date(cls, v):
        if not re.match(r"^(0[1-9]|1[0-2])\/[0-9]{2}$", v):
            raise ValueError('Expiration date must be in MM/YY format')
        # Additional validation to ensure the date is not in the past could be added here
        return v
