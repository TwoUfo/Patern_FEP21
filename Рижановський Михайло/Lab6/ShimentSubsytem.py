import sqlite3


class Provider:
    db_connection = sqlite3.connect("lab6.db")
    db_cursor = db_connection.cursor()

    def __init__(self, provider, price):
        self.provider = provider
        self.price = price

    @classmethod
    def add_provider(cls, provider, price):
        cls.db_cursor.execute('''
            SELECT COUNT(*) FROM Providers WHERE name = ?
        ''', (provider,))
        count = cls.db_cursor.fetchone()[0]

        if count == 0:
            cls.db_cursor.execute('''
                INSERT INTO Providers (name, price) VALUES (?, ?)
            ''', (provider, price))
            cls.db_connection.commit()
            return True
        else:
            print(f"Provider with name '{provider}' already exists in the database.")
            return False

    @classmethod
    def get_provider_price(cls, provider):
        cls.db_cursor.execute('''
            SELECT price FROM Providers WHERE name = ?
        ''', (provider,))
        result = cls.db_cursor.fetchone()

        if result:
            return result[0]
        else:
            raise ValueError(f"Provider '{provider}' not found in the database")


class Shipment(Provider):
    def __init__(self, provider: Provider, shipment_price, price):
        super().__init__(provider, price)
        self.provider = provider
        self.shipment_price = shipment_price

    @classmethod
    def create_shipment(cls, provider, shipment_price):
        cls.db_cursor.execute('''
            UPDATE Providers
            SET shipment_price = ?
            WHERE name = ?
        ''', (shipment_price, provider))
        cls.db_connection.commit()
        return f"Shipment created with provider: {provider}, Total Price: {shipment_price}"

