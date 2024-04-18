from fastapi import APIRouter, HTTPException
from schemas.products import Product, ProductCreate, products
product_router = APIRouter()

# create product
# list a product
# edit a product
# delete a product

# create product
# auto increment d id
# 
@product_router.post('/', status_code=201)
def create_product(payload: ProductCreate):
    product_id = len(products) + 1
    # create d product
    new_product = Product(
        id=product_id,
        name=payload.name,
        price=payload.price,
        quantity_avaliable=payload.quantity_avaliable
    )
    # add d created product to product array using append
    # products.append(new_product) -- we don't nid append cos we nid mapping
    products[product_id] = new_product
    
    # return the messge
    return {
        "message": "product added successfully", 'data':  new_product
    }
    
    
# get all product
@product_router.get('/', status_code=200)
def get_products():
    return {"message": "success", 'data': products
                }
