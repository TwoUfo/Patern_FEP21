from app.schemas.ships import LightWeightShip, MediumWeightShip, HeavyWeightShip


class ShipFactory:
    @staticmethod
    def create_ship(ship_data):
        total_weight_capacity = ship_data.get('total_weight_capacity')

        if total_weight_capacity <= 2000:
            return LightWeightShip(**ship_data)
        elif total_weight_capacity <= 4000:
            return MediumWeightShip(**ship_data)
        elif total_weight_capacity <= 6000:
            return HeavyWeightShip(**ship_data)
        else:
            raise ValueError(f"Invalid ship total weight capacity: {total_weight_capacity}")
