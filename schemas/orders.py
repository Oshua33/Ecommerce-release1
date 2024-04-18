from pydantic import BaseModel
# from schemas.products import Product

# class order
class Order(BaseModel):
    id: int
    customer_id: int
    items: list[int]
    #  list[product] -- cos listing we need the products

class OrderCreate(BaseModel):
    customer_id: int
    items: list[int]
    #  list[product] -- cos creating we need the int cos of items nos.
    
orders  = [
        Order(id=1, customer_id=1, items=[1,2,3]), 
    ]
    
# anoda way. 
# orders: list[Order] = [
#         Order(id=1, customer_id=1, items=[1,2,3]), 
#         Order(id=1, customer_id=1, items=[1,2,3]), 
# ]
    
    
    
# sample orders like dict but list of arrays
# orders: list[Order] = [
#     Order(id=1, username="johnson", address="opebi allen str"),
#     Order(id=2, username="mary", address="micon egbeda str"),
#     Order(id=3, username="Doe", address="mamie army str")
#     ]

