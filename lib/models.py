import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String, Integer, ForeignKey, Table)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref


Base = declarative_base()
engine = create_engine('sqlite:///db/inventory.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

product_supplier=Table(
    'product_suppliers',
    Base.metadata,
    Column('id', Integer(), primary_key=True),
    Column('product_id', ForeignKey('products.id')),
    Column('supplier_id', ForeignKey('suppliers.id')),
    extend_existing=True,
)

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer)

    suppliers=relationship('Supplier', secondary=product_supplier, back_populates='products')
    braches=relationship('Branch', backref=backref('product'))

    def __repr__(self):
        return f'Product: {self.name}, Price: {self.price} Kes'

    
class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    
    products=relationship('Product', secondary=product_supplier, back_populates='suppliers')
    braches=relationship('Branch', backref=backref('supplier'))
    
    def __repr__(self):
        return f'Supplier: {self.name}'
    
class Branch(Base):
    __tablename__ = 'branches'
    
    id = Column(Integer, primary_key=True)
    branch_number = Column(Integer)
    
    product_id = Column(Integer, ForeignKey('products.id'))
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
       
    def __repr__(self):
        return f'Review(id={self.id},'+\
            f'Name={self.name})'
                    
    
