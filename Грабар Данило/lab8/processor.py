from person import Person, UserRole
from student import Student
from proffesor import Professor
from manager import Manager
from visitor import AssessVisitor


class ProcessorAssessVisitor(AssessVisitor):
    def get_all_moves(self):
        pass

    def visit_student(self, student):
        pass

    def visit_professor(self, professor):
        pass


class Processor:
    def __init__(self):
        self.assess_visitor = ProcessorAssessVisitor()

    def process_staff(self, person: Person):
        if person.role == UserRole.STUDENT:
            self.process_student(Student(id=person.id, first_name=person.first_name, surname=person.surname,
                                         research_score=0, academic_score=0, visited_lectures=[]))
        elif person.role == UserRole.PROFESSOR:
            self.process_professor(Professor(id=person.id, first_name=person.first_name, surname=person.surname,
                                             research_score=0, academic_score=0, conduct_lectures=[]))

    def process_student(self, student: Student):
        professor_academic_score = 85
        student.perform_research({"task1": 5, "task2": 8})
        student.perform_studying(professor_academic_score)
        self.assess_visitor.visit_student(student)

    def process_professor(self, professor: Professor):
        professor.perform_research(["paper1", "paper2"])
        professor.conduct_classes("lecture", [Student(id=1, first_name="John", surname="Doe",
                                                      research_score=0, academic_score=75, visited_lectures=[1, 2, 3])])
        self.assess_visitor.visit_professor(professor)

    def process_manager(self, manager: Manager):
        manager.assess_staff(manager, self.assess_visitor)
