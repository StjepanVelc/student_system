from dataclasses import dataclass
from student_system.models.base import BaseModel


@dataclass
class Student(BaseModel):
    name: str = ""
    age: int = 0
    city: str = ""
    index_number: str = ""
    average_grade: float = 0.0
