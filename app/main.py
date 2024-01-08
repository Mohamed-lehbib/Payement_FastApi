from fastapi import FastAPI, HTTPException, Depends
from datetime import datetime
from sqlalchemy.orm import Session
from pydantic import BaseModel
from . import model, schemas
from .database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_client", response_model=schemas.ClientBase)
def create_client(client: schemas.ClientBase, db: Session = Depends(get_db)):
    # Check if client already exists
    db_client = db.query(model.Client).filter(model.Client.id_number == client.id_number).first()
    if db_client:
        raise HTTPException(status_code=400, detail="Client already exists")

    new_client = model.Client(**client.dict())
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client


@app.post("/create_account", response_model=schemas.AccountBase)
def create_account(account: schemas.AccountBase, db: Session = Depends(get_db)):
    db_account = db.query(model.Account).filter(model.Account.account_number == account.account_number).first()
    if db_account:
        raise HTTPException(status_code=400, detail="Account already exists")
    new_account = model.Account(**account.dict())
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account

@app.get("/account_balance/{account_number}", response_model=schemas.AccountBase)
def get_account_balance(account_number: str, db: Session = Depends(get_db)):
    account = db.query(model.Account).filter(model.Account.account_number == account_number).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@app.post("/create_card", response_model=schemas.CardBase)
def create_card(card: schemas.CardBase, db: Session = Depends(get_db)):
    db_card = db.query(model.Card).filter(model.Card.card_number == card.card_number).first()
    if db_card:
        raise HTTPException(status_code=400, detail="Card already exists")
    new_card = model.Card(**card.dict())
    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    return new_card

@app.get("/card_balance/{card_number}", response_model=schemas.CardBase)
def get_card_balance(card_number: str, db: Session = Depends(get_db)):
    card = db.query(model.Card).filter(model.Card.card_number == card_number).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return card

@app.post("/deposit_to_card")
def deposit_to_card(card_number: str, deposited_amount: float, db: Session = Depends(get_db)):
    # Fetch the card details
    card = db.query(model.Card).filter(model.Card.card_number == card_number).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")

    # Check for a valid deposit amount (greater than 0)
    if deposited_amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid deposit amount")

    # Update the card balance
    card.balance += deposited_amount

    # Commit the changes to the database
    db.commit()

    return {"message": "Deposit successful", "new_balance": card.balance}

class PaymentData(BaseModel):
    card_number: str
    owner: str
    cvv: str
    expiration_date: str
    account_number: str
    amount: float

@app.post("/make_payment")
def make_payment(card_number: str, owner: str, cvv: str, expiration_date: str, account_number: str, amount: float, db: Session = Depends(get_db)):
    # Fetch the card details
    card = db.query(model.Card).filter(model.Card.card_number == card_number).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")

    # Check if the provided owner name, cvv, and expiration date match the card details
    if card.owner != owner or card.cvv != cvv or card.expiration_date != expiration_date:
        raise HTTPException(status_code=400, detail="Card details do not match")

    # Fetch the account details
    account = db.query(model.Account).filter(model.Account.account_number == account_number).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    # Check for sufficient balance
    if card.balance < amount:
        raise HTTPException(status_code=400, detail="Insufficient balance on card")

    # Proceed with the payment
    card.balance -= amount
    account.balance += amount
    db.commit()
    return {"message": "Payment successful"}
