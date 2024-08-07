from datetime import time

from fastapi import Query, HTTPException
from app.orders.config_orders import START_WALK_TIME, END_WALK_TIME


def validate_walk_time(walk_time: time = Query(...,
                                               description=f"Время начала прогулки (доступно с {START_WALK_TIME} до "
                                                           f"{END_WALK_TIME}). Прогулка может начинаться либо в начале "
                                                           f"часа, либо в половину.",
                                               example="07:00"
                                               )) -> time:
    if walk_time.minute not in [0, 30]:
        raise HTTPException(status_code=400, detail=f"Время прогулки должно приходиться на начало часа или получаса")
    if not (START_WALK_TIME <= walk_time <= END_WALK_TIME):
        raise HTTPException(status_code=400,
                            detail=f"Прогулки могут быть запланированы только с {START_WALK_TIME} до {END_WALK_TIME}")
    return walk_time
