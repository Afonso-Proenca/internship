from typing import Optional

from pydantic import BaseModel, Field


class Item(BaseModel):
    id: int
    name: str
    price: float

 # task 3 - Item creation currently allows names that are too short. Review the expected behavior, minimum of three characters, and add appropriate validation.

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=3)  
    price: float

class ItemUpdate(BaseModel): 
    name: Optional[str] = Field(None, min_length=3)  # task 3
    price: Optional[float] = None