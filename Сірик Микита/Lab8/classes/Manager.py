from classes.AssessVisitor import AssessVisitor
from classes.Person import Person, PersonInfo


class Manager(Person):

    def __init__(self, person_info: PersonInfo):
        super().__init__(person_info)

    def assess_staff(self, person: Person, assess_visitor: AssessVisitor):
        # TODO: Implement assess staff logic
        pass
