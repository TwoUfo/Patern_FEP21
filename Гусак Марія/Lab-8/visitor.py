from person import *
from abc import ABC, abstractmethod
from multipledispatch import dispatch


class AssessVisitor(ABC):
    @abstractmethod
    def visit_student(self, student: Student):
        pass

    @abstractmethod
    def visit_professor(self, professor: Professor):
        pass


class ApplyGrant(AssessVisitor):
    @dispatch(Student)
    def visit_student(self, student: Student):
        print(f"Grant applied to student {student.get_info()}")

    @dispatch(Professor)
    def visit_professor(self, professor: Professor):
        print(f"Grant applied to professor {professor.get_info()}")



class MakeCompliant(AssessVisitor):
    @dispatch(Student)
    def visit_student(self, student: Student):
        print(f"Student {student.get_info()} made compliant")

    @dispatch(Professor)
    def visit_professor(self, professor: Professor):
        print(f"Professor {professor.get_info()} made compliant")

