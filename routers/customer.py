from fastapi import APIRouter, HTTPException
from schemas.customer import Customer, CustomerCreate, customers

customer_router = APIRouter()

# create customer
# list customers
# edit customer
# delete customer

# create customer, with sattus code of 201 for postmethod
# we include a payload of d customercreate
# create a customer-id - auto generate id
# d new customer = customerclass(auto id, destructing of customercreate)
# append to add it to previous customers list
@customer_router.post('/',status_code=201)
def create_customer(payload: CustomerCreate):
    customer_id = len(customers) + 1
    new_customer = Customer(
        id=customer_id, 
        username=payload.username,
        address=payload.address
        )
    customers.append(new_customer)
    return {"message": "customer created successfully", 'data': new_customer}


# list customers
@customer_router.get('/', status_code=200)
def get_customers():
    return {"message": "success", 'data': customers}


# edit customer, pass the customer_id, and status code of 200
# we also pass the customercreate payload so dey can't change id. in d put()
# set curr_customer to None
# get d customer, iterate thru a list. using for loop
# den if d curr_customer not found raise httpexception
# den, if not found we take in d details of username, address
@customer_router.put('/{customer_id}', status_code=200)
def edit_customer(customer_id:int, payload: CustomerCreate):
    current_customer = None
    
    for customer in customers:
        if customer.id == customer_id:
            current_customer = customer
            break
        
    if not current_customer:
        raise HTTPException(status_code=400, detail="customer not found")
    current_customer.username = payload.username
    current_customer.address = payload.address
    return {"message": "customer edited successfully", 'data': current_customer}
    
    
        
            
    
    