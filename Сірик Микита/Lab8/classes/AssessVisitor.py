from classes.Professor import Professor
from classes.Student import Student


class AssessVisitor:

    def __init__(self):
        pass

    def visit_student(self, student: Student):
        student.accept(self)

    def visit_professor(self, professor: Professor):
        professor.accept(self)
