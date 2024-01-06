# schemas.py
from pydantic import BaseModel, constr
from datetime import datetime

class ClientBase(BaseModel):
    id_number: constr(min_length=10, max_length=10)
    first_name: str
    last_name: str

class AccountBase(BaseModel):
    account_number: constr(min_length=16, max_length=16)
    balance: float
    owner_id: constr(min_length=10, max_length=10)

class CardBase(BaseModel):
    card_number: str  # Add regex for validation if needed
    owner: str
    cvv: str
    expiration_date: datetime
    balance: float
