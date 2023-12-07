import sqlite3

class Product:
    def __init__(self, product_name, amount, price):
        self.product_name = product_name
        self.amount = amount
        self.price = price

    def add_product(self):
        with sqlite3.connect("lab6.db") as db_connection:
            db_cursor = db_connection.cursor()

            db_cursor.execute('''
                INSERT INTO Products (product_name, amount, price) VALUES (?, ?, ?)
            ''', (self.product_name, self.amount, self.price))

    def update_product(self, amount):
        with sqlite3.connect("lab6.db") as db_connection:
            db_cursor = db_connection.cursor()

            db_cursor.execute('''
                UPDATE Products SET amount = ? WHERE product_name = ?
            ''', (amount, self.product_name))

class ProductStock(Product):
    def __init__(self, product_name, amount):
        super().__init__(product_name, amount, 0)  # Assuming the price is not needed in the Stock class

    def select_stock(self):
        with sqlite3.connect("lab6.db") as db_connection:
            db_cursor = db_connection.cursor()

            db_cursor.execute('''
                SELECT amount FROM Products WHERE product_name = ?
            ''', (self.product_name,))

            result = db_cursor.fetchone()
            return result[0] if result else 0

    def update_stock(self):
        self.update_product(self.select_stock() - self.amount)



