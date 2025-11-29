class StudentReport:
    def __init__(self, database):
        self.db = database

    def generate(self):
        print("\n--- STUDENT REPORT ---\n")
        for s in self.db.students:
            print(f"{s['name']} ({s['age']}), from {s['city']}")
