
from pathlib import Path
import sqlite3
from student_system.data.repository import JsonRepository
from student_system.models import professor
from student_system.models.student import Student

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
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS professors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        department TEXT,
        subject TEXT,
        place_of_residence TEXT
        )
        """)
        
        self.conn.commit()
    def add(self, student,) -> Student:
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, age, city, index_number, average_grade) VALUES (?, ?, ?, ?, ?)",
            (student.name, student.age, student.city, student.index_number, student.average_grade)
        )
        self.conn.commit()
        return student
    
    def _insert_professor(self, professor) -> professor.Professor:
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO professors (name, department, subject, place_of_residence) VALUES (?, ?, ?, ?)",
            (professor.name, professor.department, professor.subject, professor.place_of_residence)
        )
        self.conn.commit()
        return professor
        

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
    
    def add_professor(self, **kwargs) -> professor.Professor:
        prof = professor.Professor(**kwargs)
        return self._insert_professor(prof)
    
    def list_professors(self):

        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM professors")

        rows = cursor.fetchall()

        return [
            professor.Professor(
            name=row[1],
            department=row[2],
            subject=row[3],
            place_of_residence=row[4],
            id=row[0]
            )
            for row in rows
        ]
    
    def search_professors(self, query: str):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM professors WHERE name LIKE ? OR department LIKE ? OR subject LIKE ? OR place_of_residence LIKE ?",
            (f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%")
        )
        rows = cursor.fetchall()
        return [
            professor.Professor(
                name=row[1],
                department=row[2],
                subject=row[3],
                place_of_residence=row[4],
                id=row[0]
            )
            for row in rows
        ]
