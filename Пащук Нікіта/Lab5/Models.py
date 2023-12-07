from pydantic import BaseModel


class CreditCardModel(BaseModel):
    account_number: str
    client: str
    credit_limit: int
    grace_period: int
    cvv: str


class BankInfoModel(BaseModel):
    bank_name: str


class BankCustomerModel(BaseModel):
    contact_info: str
    birth_date: str
    employment: str
    income_per_year: int


class CreditHistoryModel(BaseModel):
    sender: str
    recipient: str
    amount: int
