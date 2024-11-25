from src.database import BaseModel
from dataclasses import dataclass

@dataclass
class Book(BaseModel):
    title : str
    author: str
    year: int
    status: bool = True
