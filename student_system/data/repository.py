from __future__ import annotations

from typing import Generic, TypeVar, List, Callable, Optional, Type
from pathlib import Path
import json

from student_system.models.base import BaseModel

T = TypeVar("T", bound=BaseModel)


class JsonRepository(Generic[T]):
    """Generički CRUD repozitorij nad jednim JSON fajlom."""

    def __init__(self, model_cls: Type[T], file_path: Path) -> None:
        self.model_cls = model_cls
        self.file_path = file_path
        self._items: List[T] = []
        self.load()

    # ----- low level -----
    def load(self) -> None:
        if not self.file_path.exists():
            self._items = []
            return

        with self.file_path.open("r", encoding="utf-8") as f:
            raw = json.load(f)
        self._items = [self.model_cls.from_dict(item) for item in raw]

    def save(self) -> None:
        data = [item.to_dict() for item in self._items]
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        with self.file_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    # ----- CRUD -----
    def add(self, obj: T) -> T:
        self._items.append(obj)
        self.save()
        return obj

    def all(self) -> List[T]:
        return list(self._items)

    def get(self, obj_id: str) -> Optional[T]:
        for item in self._items:
            if item.id == obj_id:
                return item
        return None

    def update(self, obj: T) -> None:
        for idx, item in enumerate(self._items):
            if item.id == obj.id:
                self._items[idx] = obj
                self.save()
                return

    def delete(self, obj_id: str) -> None:
        self._items = [item for item in self._items if item.id != obj_id]
        self.save()

    # ----- naprednije -----
    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        return [item for item in self._items if predicate(item)]

    def search(self, query: str, *fields: str) -> List[T]:
        q = query.lower()
        result = []
        for item in self._items:
            for field in fields:
                value = getattr(item, field, "")
                if q in str(value).lower():
                    result.append(item)
                    break
        return result
