from fastapi import APIRouter, Depends
from schemas.orders import orders, Order, OrderCreate
from services.orders import OrderService, order_service

order_router = APIRouter()

# list orders
# create orders

@order_router.get('/', status_code=200)
def get_orders():
    # response will be d order-passer service for our mapping
    response = order_service.order_parser(orders)
    return {"message": "orders list success", 'data': response}

# create orders
# 1. auto increase id
# 2. new order -> Order class
# 3. append new order to orders
@order_router.post('/', status_code=201)
def create_order(payload: OrderCreate = Depends(order_service.check_avalibality)):
# def create_order(customer_id:int, product_ids: list[int] = Depends(order_service.check_avalibality)):
    customer_id: int = payload.customer_id
    product_ids: list[int] = payload.items
    # get current order_id
    order_id = len(orders) + 1
    new_order = Order(
        id=order_id,
        customer_id=customer_id,
        items=product_ids
    )
    
    orders.append(new_order) 
    
    return {"message": "orders created success", 'data': new_order}
    
    