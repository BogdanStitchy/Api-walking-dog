from datetime import date, time, datetime, timedelta
import pytest
from fastapi import status

from app.orders.config_orders import START_WALK_TIME, END_WALK_TIME
from app.orders.dao import OrdersDAO


@pytest.mark.asyncio
@pytest.mark.parametrize("expected_status_code, apartment_number, pet_name, pet_breed, walk_date, walk_time",
                         [(status.HTTP_201_CREATED, "101", "Рекс", "Лабрадор", date(2024, 8, 11), time(10, 0)),
                          (status.HTTP_201_CREATED, "202", "Бобик", "Пудель", date(2024, 8, 11), time(10, 0)),
                          # Попытка добавить на уже занятое время
                          (status.HTTP_409_CONFLICT, None, "Рекс", "Лабрадор", date(2024, 8, 11), time(10, 0)),
                          # Попытка добавить на 10:45 минут (ошибка валидации)
                          (status.HTTP_400_BAD_REQUEST, None, "Рекс", "Лабрадор", date(2024, 8, 11),
                           time(10, 45)),
                          # Попытка добавить раньше времени начала прогулок (START_WALK_TIME - 2 часа)
                          (status.HTTP_400_BAD_REQUEST, None, "Рекс", "Лабрадор", date(2024, 8, 11),
                           (datetime.combine(datetime.today(), START_WALK_TIME) - timedelta(hours=2)).time()),
                          # Попытка добавить позже времени начала прогулок (END_WALK_TIME + 2 часа)
                          (status.HTTP_400_BAD_REQUEST, None, "Рекс", "Лабрадор", date(2024, 8, 11),
                           (datetime.combine(datetime.today(), END_WALK_TIME) + timedelta(hours=2)).time()),
                          # Некорректный формат времени
                          (status.HTTP_422_UNPROCESSABLE_ENTITY, 101, "Рекс", "Лабрадор", date(2024, 8, 7),
                           "invalid_time"),
                          ])
async def test_endpoint_add_order(async_client, expected_status_code, apartment_number, pet_name, pet_breed,
                                  walk_date, walk_time):
    response = await async_client.post("/orders/add_order", params={
        "apartment_number": apartment_number,
        "pet_name": pet_name,
        "pet_breed": pet_breed,
        "walk_date": walk_date,
        "walk_time": walk_time
    })
    assert response.status_code == expected_status_code


@pytest.mark.asyncio
async def test_endpoint_get_orders(async_client, clear_db_table_order, start_redis_for_method_with_cache):
    count_addition = 2
    apartment_number, pet_name, pet_breed, walk_date, walk_time = (
        "101", "Рекс", "Лабрадор", date(2024, 8, 11), time(10, 0))
    for i in range(count_addition):
        await OrdersDAO.add(apartment_number=apartment_number,
                            pet_name=pet_name,
                            pet_breed=pet_breed,
                            walk_date=walk_date,
                            walk_time=walk_time)
    response = await async_client.get(f"/orders?walk_date={walk_date}")
    assert len(response.json()) == count_addition


@pytest.mark.asyncio
async def test_endpoint_delete_order(async_client, clear_db_table_order, start_redis_for_method_with_cache):
    apartment_number, pet_name, pet_breed, walk_date, walk_time = (
        "101", "Рекс", "Лабрадор", date(2024, 8, 11), time(10, 0))
    await OrdersDAO.add(apartment_number=apartment_number,
                        pet_name=pet_name,
                        pet_breed=pet_breed,
                        walk_date=walk_date,
                        walk_time=walk_time)
    response_before_delete = await async_client.get(f"/orders?walk_date={walk_date}")
    assert len(response_before_delete.json()) == 1
    response_delete = await async_client.delete(f"/orders/{response_before_delete.json()[0]['id']}")
    assert response_delete.status_code == 204
    response_after_delete = await async_client.get(f"/orders?walk_date={walk_date}")
    assert len(response_after_delete.json()) == 0
