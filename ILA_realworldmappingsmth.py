class Student:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self):
        self.students = []
        self.count = 0

    def add_student(self, student):
        if self.count < 60:
            self.students.append(student)
            self.count += 1
