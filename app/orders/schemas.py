from pydantic import BaseModel
from datetime import date, time


class SOrderRead(BaseModel):
    id: int
    apartment_number: int
    pet_name: str
    pet_breed: str
    walk_date: date
    walk_time: time
