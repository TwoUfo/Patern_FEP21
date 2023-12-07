from classes.Person import Person


class Student(Person):

    def __init__(self, id: int, first_name: str, second_name: str, role):
        super().__init__(id, first_name, second_name, role)
