from datetime import time

from fastapi import Query
from app.orders.config_orders import START_WALK_TIME, END_WALK_TIME
from app.orders.exceptions import UncorrectedTimeOrderHTTPException, TimeIntervalOrderHTTPException


def validate_walk_time(walk_time: time = Query(...,
                                               description=f"Время начала прогулки (доступно с {START_WALK_TIME} до "
                                                           f"{END_WALK_TIME}). Прогулка может начинаться либо в начале "
                                                           f"часа, либо в половину.",
                                               example="07:00"
                                               )) -> time:
    if walk_time.minute not in [0, 30]:
        raise UncorrectedTimeOrderHTTPException
    if not (START_WALK_TIME <= walk_time <= END_WALK_TIME):
        raise TimeIntervalOrderHTTPException
    return walk_time
