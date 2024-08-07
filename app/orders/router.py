from datetime import date, time
from fastapi import APIRouter, Response, status, Depends, Query

from app.dao.exception import DaoMethodException
from app.orders.dao import OrdersDAO
from app.orders.exceptions import DeletingOrderHTTTPException, AddingOrderHTTTPException, GettingOrdersHTTTPException, \
    BusyWalkingTimeHTTPException
from app.orders.utils import validate_walk_time
from app.orders.schemas import SOrderRead

from app.orders.config_orders import POSSIBLE_WALKING_TIME

router = APIRouter(
    prefix="/orders",
    tags=["Заказы"]
)


@router.get("")
async def get_orders(walk_date: date) -> list[SOrderRead]:
    try:
        returning_value = await OrdersDAO.get_all(walk_date=walk_date)
    except DaoMethodException:
        raise GettingOrdersHTTTPException
    return returning_value


@router.post("/add_order")
async def add_order(
        apartment_number: str = Query(..., description="Номер квартиры"),
        pet_name: str = Query(..., description="Имя питомца"),
        pet_breed: str = Query(..., description="Порода питомца"),
        walk_date: date = Query(...,
                                description="Дата прогулки",
                                example="2024-08-07"
                                ),
        walk_time: time = Depends(validate_walk_time)
):
    try:
        existing_orders_for_selected_date = await OrdersDAO.get_all(walk_date=walk_date, walk_time=walk_time)
    except DaoMethodException:
        raise GettingOrdersHTTTPException

    if len(existing_orders_for_selected_date) < 2:
        try:
            await OrdersDAO.add(apartment_number=apartment_number,
                                pet_name=pet_name,
                                pet_breed=pet_breed,
                                walk_date=walk_date,
                                walk_time=walk_time)
        except DaoMethodException:
            raise AddingOrderHTTTPException
    else:
        raise BusyWalkingTimeHTTPException
    return Response(status_code=status.HTTP_201_CREATED)


@router.delete("/{order_id}")
async def delete_order(order_id: int) -> Response:
    try:
        await OrdersDAO.delete(id=order_id)
    except DaoMethodException:
        raise DeletingOrderHTTTPException
    return Response(status_code=status.HTTP_204_NO_CONTENT)
