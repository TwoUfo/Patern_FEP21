from AssessVisitor import AssessVisitor


class Person:

    def __init__(self, id: int, first_name: str, second_name: str, role) -> None:
        self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.role = role

    def get_info(self) -> str:
        pass

    def accept(self, assess_visitor: AssessVisitor):
        pass
