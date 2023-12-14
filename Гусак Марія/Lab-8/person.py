from abc import ABC, abstractmethod
from multipledispatch import dispatch
from typing import List
from enum import Enum

class Role(Enum):
    STUDENT = "student"
    PROFESSOR = "professor"
    ADMINISTRATION_STAFF = "administration_staff"

class IPerson(ABC):

    @abstractmethod
    def get_info(self) -> str:
        pass

    @abstractmethod
    def accept(self, assess_visitor):
        pass

class Person:
    def __init__(self, id: int, first_name: str, second_name: str, role: Role):
        self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.role = role

    def get_info(self) -> str:
        return f"{self.first_name} {self.second_name}, Role: {self.role}"

    def accept(self, assess_visitor):
        pass

class Student(Person):
    def __init__(self, academic_score: int, visited_lectures: int, id: int, first_name: str, second_name: str,
                 role: Role):
        super().__init__(id, first_name, second_name, role)
        self.academic_score = academic_score
        self.visited_lectures = visited_lectures

    def get_info(self) -> str:
        return f"{self.first_name} {self.second_name}, Role: {self.role}"

    def accept(self, assess_visitor):
        assess_visitor.visit_student(self)


    def perform_research(self):
        research_score ={
        "id": self.id,
        "first_name": self.first_name,
        "second_name": self.second_name,
        "academic_score": self.academic_score,
        "visited_lectures": self.visited_lectures
        }
        return research_score

    def perform_studying(self):
        studying_rate = (self.academic_score + self.visited_lectures) / 2
        return studying_rate

class Professor(Person):
    def __init__(self, academic_score: int, id: int, first_name: str, second_name: str,
                 role: Role):
        super().__init__(id, first_name, second_name, role)
        self.academic_score = academic_score

    def get_info(self) -> str:
        return f"{self.first_name} {self.second_name}, Role: {self.role}"

    def accept(self, assess_visitor):
        assess_visitor.visit_professor(self)

    def perform_research(self):
        research_score = {
            "id": self.id,
            "first_name": self.first_name,
            "second_name": self.second_name,
            "academic_score": self.academic_score
        }
        return research_score

    def conduct_classes(self, students: List[Student]):
        for student in students:
            student.perform_studying()

class Manager(Person):
    def __init__(self, person: Person, assess_visitor, id: int, first_name: str, second_name: str, role: Role):
        super().__init__(id, first_name, second_name, role)
        self.person = person
        self.assess_visitor = assess_visitor

    def assess_staff(self, person: Person, assess_visitor):
        person.accept(assess_visitor)

    def get_info(self) -> str:
        return f"{self.first_name} {self.second_name}, Role: {self.role}"


