from student_system.models.student import Student


class StudentFileReader:
    def __init__(self, path):
        self.path = path

    def load_students(self):
        students = []
        with open(self.path, "r", encoding="utf-8") as file:
            for line in file:
                name, age, city = line.strip().split(",")
                students.append(Student(name, age, city))
        return students
