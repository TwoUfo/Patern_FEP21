import unittest
from person import PersonRole
from Student import Student
from Professor import Professor
from Manager import Manager
from main import Processor


class TestProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = Processor()

    def test_process_student(self):
        student = Student(id=1, first_name="Andriy", second_name="Cumbal", research_score=23, academic_score=75,
                      visited_lectures=10)  
        self.processor.process_student(student)

    def test_process_professor(self):
        professor = Professor(id=101, first_name="Danylo", second_name="Chornui", research_score=0, academic_score=90,
                              conduct_lectures=1)
        self.processor.process_professor(professor)

    def test_process_manager(self):
        manager = Manager(id=201, first_name="Svytoslav", surname="Supryn", role=PersonRole.MANAGER)
        self.processor.process_manager(manager)


if __name__ == '__main__':
    unittest.main()