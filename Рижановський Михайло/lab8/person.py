from enum import Enum, auto
from dataclasses import dataclass
from visitor import AssessVisitor

class PersonRole(Enum):
    STUDENT = auto()
    PROFESSOR = auto()
    MANAGER = auto()

@dataclass
class Person():
    id: int
    first_name: str
    second_name: str
    role: Enum

    def get_info(self):
        return (f'Person INfo'
                f"id: {self.id}\n"
                f"first name: {self.first_name}\n"
                f"surname: {self.second_name}\n"
                f"Person role: {self.role}")
    
    def accept(self, assess_visitor: AssessVisitor):
        if self.role == PersonRole.STUDENT:
            assess_visitor.visit_student(self)
        elif self.role == PersonRole.PROFESSOR:
            assess_visitor.visit_professor(self)
