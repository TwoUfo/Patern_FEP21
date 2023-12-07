from classes.AssessVisitor import AssessVisitor
from classes.Person import Person, PersonInfo
from dataclasses import dataclass


@dataclass
class StudentInfo:
    research_score: dict
    academic_score: int
    visited_lectures: int


class Student(Person):

    def __init__(self, person_info: PersonInfo, student_info: StudentInfo) -> None:
        super().__init__(person_info)
        self.research_score = student_info.research_score
        self.academic_score = student_info.academic_score
        self.visited_lectures = student_info.visited_lectures

    def accept(self, assess_visitor: AssessVisitor) -> None:
        # TODO: Implement accepting Visitor
        pass

    def perform_search(self, tasks: dict) -> None:
        # TODO: Implement research logic
        pass

    def perform_studying(self) -> None:
        # TODO: Implement studying logic
        pass
