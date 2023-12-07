class ShoppingCart:
    def __init__(self, item, amount, shipment_price):
        self.item = item
        self.amount = amount
        self.shipment_price = shipment_price

    def checkout(self, item_price, amount, shipment_price):
        total_price = item_price * amount + shipment_price
        return total_price


class Order(ShoppingCart):
    def __init__(self, item, amount, shipment_price):
        super().__init__(item, amount, shipment_price)

    def create_order(self, item_price):
        return self.checkout(item_price)

    def edit_order(self, new_item, new_amount):
        self.item = new_item
        self.amount = new_amount

    def find_product_price(products, product_name):
        for product in products:
            if product.name == product_name:
                return product.price
        return None
