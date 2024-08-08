from sqlalchemy import Column, Integer, String, Date, Time

from app.db.base_model import Base


class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    apartment_number = Column(String, nullable=False)
    pet_name = Column(String, nullable=False)
    pet_breed = Column(String, nullable=False)
    walk_date = Column(Date, index=True, nullable=False)
    walk_time = Column(Time, nullable=False)

    def __str__(self):
        return f"Order #{self.id}\tpet: {self.pet_name} ({self.pet_breed})"
