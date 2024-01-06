# models.py
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Client(Base):
    __tablename__ = "clients"

    id_number = Column(String(10), primary_key=True, index=True)  # 10-digit string
    first_name = Column(String)
    last_name = Column(String)

    # Relationship to Account
    accounts = relationship("Account", back_populates="owner")

class Account(Base):
    __tablename__ = "accounts"

    account_number = Column(String(16), primary_key=True, index=True)  # 16-digit string
    balance = Column(Float)
    owner_id = Column(String(10), ForeignKey('clients.id_number'))

    # Relationship to Client
    owner = relationship("Client", back_populates="accounts")

class Card(Base):
    __tablename__ = "cards"

    card_number = Column(String, primary_key=True, index=True)
    owner = Column(String)
    cvv = Column(String)
    expiration_date = Column(DateTime)
    balance = Column(Float)
