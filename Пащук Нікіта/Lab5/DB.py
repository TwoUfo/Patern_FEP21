from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

Base = declarative_base()


class TableCard(Base):
    __tablename__ = "Credit_cards"

    account_number = Column("account_number", String, primary_key=True)
    client = Column("client_name", String)
    credit_limit = Column("credit_limit", Integer)
    grace_period = Column("grace_period", Integer)
    cvv = Column("cvv", String)

    def __init__(self, client, account_number, credit_limit, grace_period, cvv):
        self.client = client
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.grace_period = grace_period
        self.cvv = cvv


class TableBankInfo(Base):
    __tablename__ = "Bank_info"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    bank_name = Column("bank_name", String)
    holder_name = Column("holder_name", String)
    account_number = Column("account_number", String, ForeignKey("Credit_cards.account_number"))
    customers = relationship("TableBankCustomer", back_populates="bank_info")

    def __init__(self, bank_name, holder_name, account_number):
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.account_number = account_number


class TableBankCustomer(Base):
    __tablename__ = "BankCustomer"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    bank_id = Column("bank_id", Integer, ForeignKey("Bank_info.id"), autoincrement=True)
    contact_info = Column("contact_info", String)
    birth_date = Column("birth_date", String)
    employment = Column("employment", String, default=None)
    income_per_year = Column("income_per_year", Integer)
    bank_info = relationship("TableBankInfo", back_populates="customers")

    def __init__(self, bank_id, contact_info, birth_date, employment, income_per_year):
        self.bank_id = bank_id
        self.contact_info = contact_info
        self.birth_date = birth_date
        self.employment = employment
        self.income_per_year = income_per_year


class TableCreditHistory(Base):
    __tablename__ = 'credit_history'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    bank_name = Column("bank_name", Integer, ForeignKey("Bank_info.bank_name"))
    sender_account_number = Column('sender_account_number', String)
    recipient_account_number = Column('recipient_account_number', String)
    amount = Column('amount', Integer)

    def __init__(self, bank_name, sender_account_number, recipient_account_number, amount):
        self.bank_name = bank_name
        self.sender_account_number = sender_account_number
        self.recipient_account_number = recipient_account_number
        self.amount = amount


engine = create_engine("sqlite:///input_data.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
session.commit()
