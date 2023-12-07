from CardSubsystem import Payment
from InventorySubsystem import ProductStock
from OrderSubSystem import Order
from ShimentSubsytem import Shipment


class OrderFacade:
    def __init__(self, card_number, cvv, balance, date, provider_name, product_name, product_amount, shipment_price,
                 total_price):
        self.balance = balance
        self.card_number = card_number
        self.cvv = cvv
        self.date = date
        self.provider_name = provider_name
        self.product_name = product_name
        self.product_amount = product_amount
        self.shipment_price = shipment_price
        self.total_price = total_price

    def process_order(self):
        try:
            card = Payment(card_number=self.card_number, balance=self.balance, cvv=self.cvv, date=self.date,
                           total_price=self.total_price)
            card.verify()
        except Exception as e:
            print(f"test1 verification failed: {str(e)}. Order not processed.")
            return

        product_stock = ProductStock(self.product_name, self.product_amount)

        try:
            current_stock = product_stock.select_stock()
        except Exception as e:
            print(f"test2 accessing stock: {str(e)}. Order not processed.")
            return

        if current_stock < self.product_amount:
            print(f"test3 stock for '{self.product_name}'. Order not processed.")
            return

        try:
            order = Order(self.product_name, self.product_amount, self.shipment_price)
        except Exception as e:
            print(f"test4 creating order: {str(e)}. Order not processed.")
            return

        try:
            shipment = Shipment.create_shipment(self.provider_name, self.shipment_price)
        except Exception as e:
            print(f"test5 creating shipment: {str(e)}. Order not processed.")
            return

        try:
            product_stock.update_stock()
        except Exception as e:
            print(f"test6 updating stock: {str(e)}. Order not processed.")
            return

        try:
            card.update_balance(self.balance, self.total_price)
        except Exception as e:
            print(f"test7 updating stock: {str(e)}. Order not processed.")
            return


        print("Order processed successfully.")

