from datetime import time

from fastapi import Query, HTTPException


def validate_walk_time(walk_time: time = Query(...,
                                               description="Время начала прогулки (доступно с 7:00 до 23:00). "
                                                           "Прогулка может начинаться либо в начале часа, "
                                                           "либо в половину.",
                                               example="07:00"
                                               )) -> time:
    if walk_time.minute not in [0, 30]:
        raise HTTPException(status_code=400, detail="Время прогулки должно приходиться на начало часа или получаса")
    if not (7 <= walk_time.hour < 23 or (walk_time.hour == 23 and walk_time.minute == 0)):
        raise HTTPException(status_code=400, detail="Прогулки могут быть запланированы только с 7 утра до 11 вечера")
    return walk_time
