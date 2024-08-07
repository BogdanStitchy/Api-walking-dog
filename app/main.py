from time import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin

from app.admin_panel.views import OrderAdmin
from app.db.base_model import engine
from app.logger import logger
from app.orders.router import router

app = FastAPI()

app.include_router(router)

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # куки
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content_Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

admin = Admin(app, engine)
admin.add_view(OrderAdmin)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # замер времени обработки каждого запроса
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info("Request execution time", extra={
        "process_time": round(process_time, 4)
    })
    return response
