from fastapi import FastAPI
from order_routes import order_router
from couriers_routes import courier_router


app=FastAPI()


app.include_router(order_router)
app.include_router(courier_router)