from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Order(Base):

    __tablename__="orders_main"

    orderId=Column(Integer,primary_key=True,index=True)
    orderItem=Column(String,index=True)
    orderQty=Column(Integer)
    orderAmt=Column(Integer)
    orderStatus=Column(String)
    custId=Column(Integer,ForeignKey('cust_main.custId'))

    cust=relationship("Customer",back_populates="order")

class Customer(Base):
    __tablename__="cust_main"

    custId=Column(Integer,primary_key=True,index=True)
    custName=Column(String,index=True)
    custPwd=Column(String)
    custEmail=Column(String)
    custPno=Column(Integer)


    order=relationship("Order",back_populates="cust")