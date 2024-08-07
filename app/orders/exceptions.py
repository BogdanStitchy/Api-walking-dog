from fastapi import HTTPException, status

from app.orders.config_orders import START_WALK_TIME, END_WALK_TIME


class OrderHTTTPException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class AddingOrderHTTTPException(OrderHTTTPException):
    detail = "Ошибка добавления заказа"


class GettingOrdersHTTTPException(OrderHTTTPException):
    detail = "Ошибка получения заказов"


class DeletingOrderHTTTPException(OrderHTTTPException):
    detail = "Ошибка удаления заказа"


class UncorrectedTimeOrderHTTPException(OrderHTTTPException):
    status_code = 400
    detail = "Время прогулки должно приходиться на начало часа или получаса"


class TimeIntervalOrderHTTPException(OrderHTTTPException):
    status_code = 400
    detail = f"Прогулки могут быть запланированы только с {START_WALK_TIME} до {END_WALK_TIME}"


