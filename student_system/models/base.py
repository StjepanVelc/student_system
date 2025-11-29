from dataclasses import dataclass, field
from typing import Any, Dict
import uuid


@dataclass
class BaseModel:
    """Osnovni model za sve entitete (Student, Professor, Record...)."""

    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def to_dict(self) -> Dict[str, Any]:
        """Pretvori objekt u dict koji se može serijalizirati u JSON."""
        return self.__dict__.copy()

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BaseModel":
        """Napravi objekt iz dict-a (npr. učitanog iz JSON-a)."""
        return cls(**data)
