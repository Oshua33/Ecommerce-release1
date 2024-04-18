from fastapi import HTTPException

from schemas.products import products, Product, ProductCreate
from schemas.orders import orders, Order, OrderCreate

from logger import logger

class OrderService:
    
    # we create order_passer to pass d orders nd map it wit produt
    @staticmethod
    def order_parser(orders):
        for order in orders:
            order_items = order.items
            new_order = []
            # iterate for prdocts to 
            for product_id in order_items:
                # get product using maping 1:, 2:, 
                product = products.get(product_id)
                # append it
                new_order.append(product)
                order.items = new_order
            return orders
                
                
    # check if order is avalible
    # we nid product ids -- loop thru product_id, but pass in payload ordercreate instead
    # if lesser dan 1 raise error else return product_ids
    @staticmethod
    def check_avalibality(payload: OrderCreate):
        # convert product_ids to payload.items
        product_ids = payload.items
        for product_id in product_ids:
        # get product_id with class
            # now we return a Product object, from the dict of product in schema. now we use .get(product_id) - to get a particular key from d dict, e.g 1: -- product_id 1.
            product: Product = products.get(product_id)
            if product.quantity_avaliable < 1:
                logger.warning("product no longer avalible")
                raise HTTPException(status_code=400, detail="product not avalible")
            product.quantity_avaliable -= 1
        return payload
        
        
    
                
order_service = OrderService()