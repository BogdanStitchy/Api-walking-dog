from sqladmin import ModelView

from app.orders.model import Orders


class OrderAdmin(ModelView, model=Orders):
    column_list = [c.name for c in Orders.__table__.c]
    name = "Заказ"
    name_plural = "Заказы"
    icon = "fa-solid fa-clipboard-list"
