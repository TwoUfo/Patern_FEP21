from classes.Person import Person, PersonInfo
from classes.AssessVisitor import AssessVisitor
from classes.Student import Student


class Professor(Person):

    def __init__(self, person_info: PersonInfo, research_score: dict, academic_score: int) -> None:
        super().__init__(person_info)
        self.research_score = research_score
        self.academic_score = academic_score

    def accept(self, assess_visitor: AssessVisitor) -> None:
        # TODO: Implement accepting Visitor
        pass

    def perform_research(self) -> None:
        # TODO: Implement research logic
        pass

    def conduct_classes(self, students: list[Student]) -> None:
        for student in students:
            student.perform_studying()
