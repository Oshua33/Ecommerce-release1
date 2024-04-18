from decimal import Decimal
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: Decimal
    quantity_avaliable: int
    
class ProductCreate(BaseModel):
    name: str
    price: Decimal
    quantity_avaliable: int
    
    # product sample db
# products = [
#     Product(id=1, name="milo", price=Decimal('100.00'), quantity_avaliable=10),
#     Product(id=2, name="dano", price=Decimal('150.00'), quantity_avaliable=5),
#     Product(id=3, name="sugar", price=Decimal('50.10'), quantity_avaliable=7),
# ]

# instead of array of list, we use dict cos we nid to map it to items
# using dict mapping
products = {
    1: Product(id=1, name="milo", price=Decimal('100.00'), quantity_avaliable=10),
    2: Product(id=2, name="dano", price=Decimal('150.00'), quantity_avaliable=1),
    3: Product(id=3, name="sugar", price=Decimal('50.10'), quantity_avaliable=7),
}
    

    