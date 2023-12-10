from classes.AssessVisitor import AssessVisitor
from classes.Professor import Professor
from classes.Student import Student


class ApplyGrant(AssessVisitor):

    def __init__(self):
        super().__init__()

    def visit_student(self, student: Student) -> None:
        # TODO: Implement applying grant logic to student
        pass

    def visit_professor(self, professor: Professor) -> None:
        # TODO: Implement applying grant logic to professor
        pass
