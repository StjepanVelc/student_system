from pathlib import Path

from student_system.data.repository import JsonRepository
from student_system.models.student import Student


class Database:
    """Centralna klasa – drži repozitorije i helper metode."""

    def __init__(self, base_dir: Path | None = None) -> None:
        if base_dir is None:
            base_dir = Path(__file__).resolve().parent.parent / "storage"

        self.base_dir = base_dir

        self.students = JsonRepository(
            Student,
            self.base_dir / "students.json",
        )

    # helper metode – lijepi interface za ostatak app-a
    def add_student(self, **kwargs) -> Student:
        student = Student(**kwargs)
        return self.students.add(student)

    def list_students(self):
        return self.students.all()

    def search_students(self, query: str):
        return self.students.search(query, "name", "city", "index_number")
