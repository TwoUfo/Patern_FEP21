using System;
using System.Collections.Generic;
using System.Text;
public enum Role
{
    Student,
    TeachingStaff,
    ResearchStaff,
    AdministrationStaff
}

public abstract class Person
{
    public int Id { get; set; }
    public string FirstName { get; set; }
    public string SecondName { get; set; }
    public Role Role { get; set; }

    public abstract string GetInfo();

    public abstract void Accept(AssessVisitor assessVisitor);
}

public class Student : Person
{
    public Dictionary<string, int> ResearchScore { get; set; }
    public int VisitedLectures { get; set; }

    public override string GetInfo()
    {
        return $"Студент - ID: {Id}, Ім'я: {FirstName} {SecondName}, Роль: {Role}";
    }

    public override void Accept(AssessVisitor assessVisitor)
    {
        assessVisitor.VisitStudent(this);
    }

    public void PerformResearch(Dictionary<string, int> tasks)
    {
        // Логіка оцінки результатів дослідження на основі завдань
        foreach (var task in tasks)
        {
            ResearchScore[task.Key] = task.Value;
        }
    }

    public void PerformStudying(params object[] args)
    {
        int participationScore = 0;
        int assignmentScore = 0;

        foreach (var arg in args)
        {
            if (arg is int)
            {
                // Припустимо, що це бали за участь
                participationScore += (int)arg;
            }
            else if (arg is string)
            {
                // Припустимо, що це бали за завдання
                int assignmentResult;
                if (int.TryParse((string)arg, out assignmentResult))
                {
                    assignmentScore += assignmentResult;
                }
            }
        }

        // Тут ви можете використовувати зібрані бали для розрахунку загального рейтингу
        int totalScore = participationScore + assignmentScore;
    }

}

public class Professor : Person
{
    public Dictionary<string, int> ResearchScore { get; set; }
    public int AcademicScore { get; set; }

    public override string GetInfo()
    {
        return $"Професор - ID: {Id}, Ім'я: {FirstName} {SecondName}, Роль: {Role}";
    }

    public override void Accept(AssessVisitor assessVisitor)
    {
        assessVisitor.VisitProfessor(this);
    }

    public void PerformResearch(params object[] args)
    {
        foreach (var arg in args)
        {
            if (arg is string)
            {
                // Припустимо, що це назва завдання або об'єкт дослідження
                string researchTask = (string)arg;

            }
            else if (arg is int)
            {
                // Припустимо, що це додаткові бали за виконання завдань
                int additionalScore = (int)arg;

                // Логіка додавання балів до AcademicScore
                AcademicScore += additionalScore;
            }
        }
    }


    public void ConductClasses(List<Student> students)
    {
        // Викликати метод студента perform_studying
        foreach (var student in students)
        {
            student.PerformStudying();
        }
    }
}

public class Manager : Person
{
    public void AssessStaff(Person person, AssessVisitor assessVisitor)
    {
        person.Accept(assessVisitor);
    }

    public override string GetInfo()
    {
        return $"Менеджер - ID: {Id}, Ім'я: {FirstName} {SecondName}, Роль: {Role}";
    }

    public override void Accept(AssessVisitor assessVisitor)
    {
        assessVisitor.VisitManager(this);
    }
}


public abstract class AssessVisitor
{
    public abstract void VisitStudent(Student student);
    public abstract void VisitProfessor(Professor professor);
    public abstract void VisitManager(Manager manager); 
}

public class ApplyGrant : AssessVisitor
{

    public override void VisitStudent(Student student)
    {
        // Логіка надання гранту для студента
        int grantAmount = CalculateGrantAmountForStudent(student);
        Console.WriteLine($"Надання {grantAmount} надано {student.GetInfo()}");
    }

    public override void VisitProfessor(Professor professor)
    {
        // Логіка надання гранту для професора
        int grantAmount = CalculateGrantAmountForProfessor(professor);
        Console.WriteLine($"Надання {grantAmount} надано {professor.GetInfo()}");
    }

    public override void VisitManager(Manager manager)
    {
        // Логіка надання гранту для менеджера
        // Додайте свою специфічну логіку тут
    }

    // Додайте інші методи та логіку за необхідності
    private int CalculateGrantAmountForStudent(Student student)
    {
        // Логіка розрахунку гранту для студента
        return student.ResearchScore.Values.Sum();
    }

    private int CalculateGrantAmountForProfessor(Professor professor)
    {
        // Логіка розрахунку гранту для професора
        return professor.AcademicScore * 10;
    }
}


// Concrete class MakeCompliant
public class MakeCompliant : AssessVisitor
{

    public override void VisitStudent(Student student)
    {
        // Логіка забезпечення відповідності для студента
        EnsureComplianceForStudent(student);
        Console.WriteLine($"{student.GetInfo()} тепер відповідає вимогам.");
    }

    public override void VisitProfessor(Professor professor)
    {
        // Логіка забезпечення відповідності для професора
        EnsureComplianceForProfessor(professor);
        Console.WriteLine($"{professor.GetInfo()} тепер відповідає вимогам.");
    }

    public override void VisitManager(Manager manager)
    {
        // Логіка забезпечення відповідності для менеджера
        // Додайте свою специфічну логіку тут
    }

    private void EnsureComplianceForStudent(Student student)
    {
        // Логіка перевірки відповідності для студента
        if (student.ResearchScore.Values.Sum() < 50)
        {
            // Якщо не відповідає вимогам, виконайте відповідні дії
            student.ResearchScore["BonusResearch"] = 10;
        }
    }

    private void EnsureComplianceForProfessor(Professor professor)
    {
        // Логіка перевірки відповідності для професора
        if (professor.AcademicScore < 80)
        {
            // Якщо не відповідає вимогам, виконайте відповідні дії
            professor.AcademicScore += 10;
        }
    }
}



public class Processor
{
    public void RunTests()
    {
        TestStudentResearch();
        TestProfessorResearch();
        TestGrantApplication();
        TestComplianceCheck();
    }

    private void TestStudentResearch()
    {
        Console.WriteLine("Поточна контрольна робота студента...");

        // Створення об'єкту Student та передавання йому деяких параметрів
        Student student = new Student
        {
            Id = 1,
            FirstName = "John",
            SecondName = "Doe",
            Role = Role.Student,
            ResearchScore = new Dictionary<string, int>(),
            VisitedLectures = 10
        };

        // Виклик методу PerformResearch для студента
        student.PerformResearch(new Dictionary<string, int> { { "Task1", 20 }, { "Task2", 15 } });

        // Перевірка, чи ResearchScore студента оновлено правильно
        Console.WriteLine("Дослідницький тест студента складено.\n");
    }

    private void TestProfessorResearch()
    {
        Console.WriteLine("Тест для професорського дослідження...");

        // Створено об'єкт Professor та передав йому деякі параметри
        Professor professor = new Professor
        {
            Id = 2,
            FirstName = "Jane",
            SecondName = "Smith",
            Role = Role.TeachingStaff,
            ResearchScore = new Dictionary<string, int>(),
            AcademicScore = 75
        };

        professor.PerformResearch("ResearchTopic1");
        Console.WriteLine("Професорський іспит складено.\n");
    }

    private void TestGrantApplication()
    {
        Console.WriteLine("Виконується тест для заявки на грант...");

        // Створив об'єкт ApplyGrant та передав йому деякі параметри
        ApplyGrant grantApplicant = new ApplyGrant();

        // Створив об'єкт Student та Professor для подання заявок на грант
        Student studentApplicant = new Student
        {
            Id = 3,
            FirstName = "Alice",
            SecondName = "Johnson",
            Role = Role.Student,
            ResearchScore = new Dictionary<string, int> { { "Task1", 30 }, { "Task2", 25 } },
            VisitedLectures = 15
        };

        Professor professorApplicant = new Professor
        {
            Id = 4,
            FirstName = "Bob",
            SecondName = "Anderson",
            Role = Role.TeachingStaff,
            ResearchScore = new Dictionary<string, int> { { "ResearchTopic1", 40 } },
            AcademicScore = 85
        };

        // Викликав методи VisitStudent та VisitProfessor для заявників на грант
        grantApplicant.VisitStudent(studentApplicant);
        grantApplicant.VisitProfessor(professorApplicant);

        Console.WriteLine("Тест заявки на грант пройдено.\n");
    }

    private void TestComplianceCheck()
    {
        Console.WriteLine("Запуск тесту для перевірки відповідності...");

        // Створив об'єкт MakeCompliant та передав йому деякі параметри
        MakeCompliant complianceChecker = new MakeCompliant();

        // Створив об'єкти Student та Professor для перевірки відповідності
        Student compliantStudent = new Student
        {
            Id = 5,
            FirstName = "Eva",
            SecondName = "Miller",
            Role = Role.Student,
            ResearchScore = new Dictionary<string, int> { { "Task1", 50 }, { "Task2", 45 } },
            VisitedLectures = 20
        };

        Professor nonCompliantProfessor = new Professor
        {
            Id = 6,
            FirstName = "Charlie",
            SecondName = "Williams",
            Role = Role.TeachingStaff,
            ResearchScore = new Dictionary<string, int> { { "ResearchTopic1", 30 } },
            AcademicScore = 70
        };

        // Викликав методи VisitStudent та VisitProfessor для перевірки відповідності
        complianceChecker.VisitStudent(compliantStudent);
        complianceChecker.VisitProfessor(nonCompliantProfessor);

        Console.WriteLine("Тест перевірки відповідності пройдено.\n");
    }
    class Program
    {
        static void Main()
        {
            Console.OutputEncoding = Encoding.UTF8;
            // Створив екземпляр класу Processor і запустив тести
            Processor processor = new Processor();
            processor.RunTests();

            Console.ReadLine();
        }
    }
}