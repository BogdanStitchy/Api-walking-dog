"""
Данный файл служит для настройки внутренних параметров для оформления заказов
"""
from datetime import datetime, timedelta, time


def __generate_time_slots(start_hour: time, end_hour: time, step_minutes: int):
    time_slots = []
    current_time = datetime.combine(datetime.today(), start_hour)
    end_time = datetime.combine(datetime.today(), end_hour)

    while current_time <= end_time:
        time_slots.append(current_time.time())
        current_time += timedelta(minutes=step_minutes)

    return time_slots


COUNT_WALKER = 2
START_WALK_TIME = time(hour=7, minute=00)
END_WALK_TIME = time(hour=23, minute=00)
WALK_DURATION_MINUTES = 30
POSSIBLE_WALKING_TIME = __generate_time_slots(START_WALK_TIME, END_WALK_TIME, WALK_DURATION_MINUTES)
