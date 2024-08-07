import pydantic
from datetime import date, time
from sqlalchemy import and_, func, insert, or_, select
from sqlalchemy.exc import SQLAlchemyError

from app.dao.exception import DaoMethodException
from app.db.base_model import async_session_maker
from app.orders.model import Orders
from app.dao.base_dao import BaseDAO


class OrdersDAO(BaseDAO):
    model = Orders

    @classmethod
    @pydantic.validate_call
    async def get_busy_time_in_selected_date(cls, selected_date: date) -> list[time]:
        try:
            async with async_session_maker() as session:
                query = select(cls.model.walk_time).filter_by(walk_date=selected_date)
                result_query = await session.execute(query)
                busy_times = result_query.scalars().all()
                print(f"{busy_times=}")
                return busy_times
        except (SQLAlchemyError, Exception) as error:
            msg = "Database Exc" if isinstance(error, SQLAlchemyError) else "Unknown Exc"
            msg += ": Cannot get meme with pagination"
            extra = {
                "selected_date": selected_date,
            }
            # logger.error(msg, extra=extra, exc_info=True)
            raise DaoMethodException(error)
