from person import Person, PersonRole

class Student(Person):
    def __init__(self, id, first_name, second_name, research_score: dict, academic_score: int, visited_lectures: int):
        super().__init__(id, first_name, second_name, PersonRole.STUDENT)
        self.research_score = research_score
        self.academic_score = academic_score
        self.visited_lectures = visited_lectures

    def accept(self):
        return self

    def perform_research(self, tasks):
        for key, value in tasks.items():
            tasks[key] = value + 15

    def perform_studying(self, *args):
        additional_scores_average = sum(args) / len(args) if args else 0

        base_studying_rate = 0.5
        academic_influence = 0.2 * self.academic_score
        lectures_influence = 0.1 * self.visited_lectures 

        studying_rate = base_studying_rate + academic_influence + lectures_influence + additional_scores_average

        print(f"Studying rate for {self.first_name} {self.second_name}: {studying_rate}")

# student = Student(id=1, first_name="John", second_name="Doe", research_score={}, academic_score=80, visited_lectures=10)
# student.perform_research({"task1": 75, "task2": 90, "task3": 85})
# student.perform_studying(75, 90, 85)
