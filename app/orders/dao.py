from sqlalchemy import and_, func, insert, or_, select
from sqlalchemy.exc import SQLAlchemyError

from app.orders.model import Orders
from app.dao.base import BaseDAO


class OrdersDAO(BaseDAO):
    model = Orders
