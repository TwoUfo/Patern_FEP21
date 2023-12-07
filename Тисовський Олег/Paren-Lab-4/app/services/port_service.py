from app.schemas.port import Port


class PortFactory:
    @staticmethod
    def create_port(port_data):
        return Port(**port_data)
