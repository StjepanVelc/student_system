from calendar import c
from pathlib import Path
import sqlite3
from student_system.data.repository import JsonRepository
from student_system.models.student import Student

connection = sqlite3.connect("students.db")
class Database:
    """Centralna klasa – drži repozitorije i helper metode."""

    def __init__(self, connection, base_dir: Path | None = None) -> None:
        if base_dir is None:
            base_dir = Path(__file__).resolve().parent.parent / "storage"
        self.conn = connection
        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        city TEXT,
        index_number TEXT,
        average_grade REAL
        )
        """)

        self.conn.commit()
    def add(self, student):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, age, city, index_number, average_grade) VALUES (?, ?, ?, ?, ?)",
            (student.name, student.age, student.city, student.index_number, student.average_grade)
        )
        self.conn.commit()
        return student
        

    # helper metode – lijepi interface za ostatak app-a
    def add_student(self, **kwargs) -> Student:
        student = Student(**kwargs)
        return self.add(student)

    def list_students(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        return [Student(*row) for row in rows]

    def search_students(self, query: str):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM students WHERE name LIKE ? OR city LIKE ? OR index_number LIKE ?",
            (f"%{query}%", f"%{query}%", f"%{query}%")
        )
        rows = cursor.fetchall()
        return [Student(*row) for row in rows]
