from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class Products(Base):
    __tablename__ = 'Products'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    product_name = Column("product_name", String)
    amount = Column("amount", Integer)
    price = Column("price", Integer)

    def __init__(self, product_name: str, amount: int, price: int):
        self.product_name = product_name
        self.amount = amount
        self.price = price


class Card(Base):
    __tablename__ = "credit_card"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    card_number = Column("card_number", String)
    balance = Column("balance", Integer)
    cvv = Column("cvv", String(3))
    date = Column("date_expired", String)

    def __init__(self, card_number: str, balance: int, cvv: int, date: int):
        self.card_number = card_number
        self.balance = balance
        self.cvv = cvv
        self.date = date


class Providers(Base):
    __tablename__ = "Providers"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    price = Column("price", Integer)
    shipment_price = Column("shipment_price", Integer)

    def __init__(self, name: str, price: int, shipment_price: int):
        self.name = name
        self.price = price
        self.shipment_price = shipment_price


engine = create_engine("sqlite:///lab6.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
