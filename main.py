from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from middleware import ecommerce_middleware
from routers.customer import customer_router
from routers.product import product_router
from routers.order import order_router
from logger import logger


app = FastAPI()
logger.info("Starting app")

# add a middleware 2nd method, and best method
app.add_middleware(BaseHTTPMiddleware, dispatch=ecommerce_middleware)

app.include_router(router=customer_router, prefix="/customers", tags=['Customers'])
app.include_router(router=product_router, prefix="/products", tags=['Products'])
app.include_router(router=order_router, prefix="/orders", tags=['Orders'])



@app.get('/')
def index():
    return{"message": "wellcome to our store"}
