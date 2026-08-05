class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_student(self):
        self.display()
        print("Course:", self.course)

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_teacher(self):
        self.display()
        print("Subject:", self.subject)
student = Student("Preethi", 20, "AIML")
teacher = Teacher("Ramesh", 35, "Python")

print("Student Details")
student.display_student()

print("\nTeacher Details")
teacher.display_teacher()