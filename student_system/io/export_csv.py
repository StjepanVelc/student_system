import csv
from pathlib import Path
from typing import Iterable, Callable

from student_system.models.student import Student


def export_students_to_csv(
    students: Iterable[Student],
    file_path: Path,
    filter_fn: Callable[[Student], bool] | None = None,
) -> None:
    """Export studenata u CSV, uz opcionalni filter (npr. prosjek > 8.0)."""
    if filter_fn is not None:
        students = [s for s in students if filter_fn(s)]

    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "age", "city", "index_number", "average_grade"])
        for s in students:
            writer.writerow(
                [s.id, s.name, s.age, s.city, s.index_number, s.average_grade]
            )
