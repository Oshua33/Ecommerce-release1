from pydantic import BaseModel

class Customer(BaseModel):
    id: int
    username: str
    address: str
    
# no id here cos we do not want d client side to send us id, id is auto generated, so we create this class
class CustomerCreate(BaseModel):
    username: str
    address: str
    
    
# create array of list of customers
# the Customer()- customer object - a class and wat our Customer object looks like
customers: list[Customer] = [
    Customer(id=1, username="johnson", address="opebi allen str"),
    Customer(id=2, username="mary", address="micon egbeda str"),
    Customer(id=3, username="Doe", address="mamie army str")
    ]

    # password_hash: str    
    # create a container for hash password. we use the password_hash
    # search how to encode a password in python or how to hash a string-- w3school