from datetime import date, time
from fastapi import APIRouter, Response, status, HTTPException, Depends, Query

from app.orders.dao import OrdersDAO
from app.orders.utils import validate_walk_time
from app.orders.schemas import SOrderRead

router = APIRouter(
    prefix="/orders",
    tags=["Заказы"]
)


@router.get("")
async def get_bookings(walk_date: date) -> list[SOrderRead]:
    returning_value = await OrdersDAO.get_all(walk_date=walk_date)

    return returning_value


@router.post("/add_order")
async def add_bookings(
        apartment_number: str = Query(..., description="Номер квартиры"),
        pet_name: str = Query(..., description="Имя питомца"),
        pet_breed: str = Query(..., description="Порода питомца"),
        walk_date: date = Query(...,
                                description="Дата прогулки",
                                example="2024-08-07"
                                ),
        walk_time: time = Depends(validate_walk_time)
):
    existing_orders_for_selected_date = await OrdersDAO.get_all(walk_time=walk_time)
    if len(existing_orders_for_selected_date) < 2:
        await OrdersDAO.add(apartment_number=apartment_number,
                            pet_name=pet_name,
                            pet_breed=pet_breed,
                            walk_date=walk_date,
                            walk_time=walk_time)
    return {"message": "Order added successfully"}


@router.delete("/{order_id}")
async def delete_booking(order_id: int):
    await OrdersDAO.delete(id=order_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
