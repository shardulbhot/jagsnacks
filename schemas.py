from pydantic import BaseModel
from typing import Optional,List


class Order(BaseModel):
    orderItem:str
    orderQty:int
    orderAmt:int
    orderStatus:str

class showCust(BaseModel):
    custName:str
    custEmail:str
    custPno:int
    order:List[Order]
    class Config():
        orm_mode=True

class showOrder(BaseModel):
    orderItem: str
    orderQty: int
    orderAmt: int
    #cust: showCust

    class Config():
        orm_mode = True

class Customer(BaseModel):
    custName:str
    custEmail:str
    custPwd:str
    custPno:int

class Login(BaseModel):
    username:str
    pwd:str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None



