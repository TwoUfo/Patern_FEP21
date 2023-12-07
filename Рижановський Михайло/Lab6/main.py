from OrderFacade import OrderFacade
from db import session, engine, Providers, Products, Card, get_db
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

app = FastAPI()

connection = engine.connect()

products = session.query(Products).all()
cards = session.query(Card).all()
providers = session.query(Providers).all()


facade = OrderFacade('c23223', '322', 200, '10/26', 'ShipX', 'Clothes', 10, 23, 50)
facade.process_order()

# @app.post("/process_order")
# def process_order(card_number, cvv, balance, date, provider_name, product_name, product_amount, db: Session = Depends(get_db)):
#     """Shipment types:
#         'New Post' cost 20
#         'ShipX' cost 10
#         'NCK' cost 25
#
#         Cards:
#         c23223,150,322,10/26
#         c232621,500,123,12/24
#
#         Products:
#         Clothes,40,100
#         Banana,87,100
#         Toys,15,43
#         Tea,23,122
#     """
#
#     facade = OrderFacade(card_number, cvv, balance, date, provider_name, product_name, product_amount)
#     facade.process_order()
#     return {"message": "Order processed successfully."}/