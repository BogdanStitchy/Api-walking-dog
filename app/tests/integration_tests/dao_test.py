from datetime import date, time

import pytest

from app.orders.dao import OrdersDAO
from app.dao.exception import DaoMethodException


@pytest.mark.asyncio
@pytest.mark.parametrize("expected_exception, apartment_number, pet_name, pet_breed, walk_date, walk_time",
                         [(None, 101, "Рекс", "Лабрадор", date(2024, 8, 11), time(10, 0)),
                          (None, 202, "Бобик", "Пудель", date(2024, 8, 12), time(10, 30)),
                          (DaoMethodException, None, "Рекс", "Лабрадор", date(2024, 8, 7), time(7, 0)),
                          # Нулевой apartment_number
                          (DaoMethodException, 101, "Рекс", "Лабрадор", "invalid_date", time(7, 0)),
                          # Неверный формат даты
                          (DaoMethodException, 101, "Рекс", "Лабрадор", date(2024, 8, 7), "invalid_time"),
                          # Неверный формат времени
                          (DaoMethodException, 101, None, "Лабрадор", date(2024, 8, 7), time(7, 0)),
                          # Нулевое имя питомца
                          ])
async def test_add_orders(expected_exception, apartment_number, pet_name, pet_breed, walk_date,
                          walk_time):
    if expected_exception is None:
        await OrdersDAO.add(apartment_number=apartment_number,
                            pet_name=pet_name,
                            pet_breed=pet_breed,
                            walk_date=walk_date,
                            walk_time=walk_time)
    else:
        with pytest.raises(expected_exception):
            await OrdersDAO.add(apartment_number=apartment_number,
                                pet_name=pet_name,
                                pet_breed=pet_breed,
                                walk_date=walk_date,
                                walk_time=walk_time)


@pytest.mark.asyncio
async def test_get_orders(clear_db_table_order):
    count_addition = 2
    apartment_number, pet_name, pet_breed, walk_date, walk_time = (
        101, "Рекс", "Лабрадор", date(2024, 8, 11), time(10, 0))
    for i in range(count_addition):
        await OrdersDAO.add(apartment_number=apartment_number,
                            pet_name=pet_name,
                            pet_breed=pet_breed,
                            walk_date=walk_date,
                            walk_time=walk_time)
    orders = await OrdersDAO.get_all(walk_date=walk_date)
    assert len(orders) == count_addition


@pytest.mark.asyncio
async def test_delete_order(clear_db_table_order):
    apartment_number, pet_name, pet_breed, walk_date, walk_time = (
        101, "Рекс", "Лабрадор", date(2024, 8, 11), time(10, 0))
    await OrdersDAO.add(apartment_number=apartment_number,
                        pet_name=pet_name,
                        pet_breed=pet_breed,
                        walk_date=walk_date,
                        walk_time=walk_time)
    orders = await OrdersDAO.get_all(walk_date=walk_date)
    assert len(orders) == 1
    await OrdersDAO.delete(id=orders[0]["id"])
    orders = await OrdersDAO.get_all(walk_date=walk_date)
    assert len(orders) == 0
