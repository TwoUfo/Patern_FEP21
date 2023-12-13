from app.schemas.ship import Ship


class ShipFactory:
    @staticmethod
    def create_ship(ship_data):
        return Ship(**ship_data)
