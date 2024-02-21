import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import (create_engine, Column, String, Integer, ForeignKey, Table)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from tabulate import tabulate

Base = declarative_base()
engine = create_engine('sqlite:///inventory.db', echo=True)
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
    item_quantity = Column(Integer)
    price = Column(Integer)
    
    suppliers=relationship('Supplier', secondary=product_supplier, back_populates='products')
    braches=relationship('Branch', backref=backref('product'))

    def __repr__(self):
        return f'Product: {self.name}, Quantity: {self.item_quantity}, Price: {self.price} Kes'

    def add_new_product(self, name, item_quantity, price):
        # Create a new product instance
        new_product = Product(name=name,item_quantity=item_quantity, price=price)
        
        # Add the new product
        session.add(new_product)
        
        # Commit changes to the database
        session.commit()
    
    def remove_product(self, name):
        # Query the database to find the product by its name
        product_to_remove =session.query(Product).filter(Product.name == name).first()
        
        if product_to_remove:
            session.delete(product_to_remove)
            session.commit()
            print(f"Product with name '{name}' removed successfully.")
        else:
            print(f"Product with name '{name}' not found.")
    
    def update_product_price(self, product_name, new_price):
        # Query the database to find the product by its name
        product_to_update = session.query(Product).filter_by(name=product_name).first()

        if product_to_update:
            # Update the product's price
            product_to_update.price = new_price

            # Commit changes to the database
            session.commit()
            print(f"Price for product '{product_name}' updated to {new_price} Kes.")
        else:
            print(f"Product with name '{product_name}' not found.")
    
    @classmethod
    def search_by_product_name(cls, product_name):
        # Query the database to find products by name
        products = session.query(cls).filter(cls.name.like(f'%{product_name}%')).all()

        if products:
            print(f"Products with name '{product_name}':")
            for product in products:
                print(f"ID: {product.id}, Name: {product.name}, Quantity: {product.item_quantity}, Price: {product.price} Kes")
        else:
            print(f"No products found with name '{product_name}'.")
       
    @classmethod
    def show_all_products(cls):
        # Query the database to retrieve all products
        all_products = session.query(cls).all()
        
        if all_products:
            table_data = []
            for product in all_products:
                table_data.append([product.id, product.name, product.item_quantity, f"{product.price} Kes"])

            headers = ["ID", "Product Name", "Quantity", "Price"]
            print("All products in the inventory:")
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
        else:
            print("No products found in the inventory.")

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    
    products=relationship('Product', secondary=product_supplier, back_populates='suppliers')
    braches=relationship('Branch', backref=backref('supplier'))
    
    def __repr__(self):
        return f'Supplier: {self.name}'
    
class Branch(Base):
    __tablename__ = 'outlets'
    
    id = Column(Integer, primary_key=True)
    branch_name = Column(String())
    
    product_id = Column(Integer, ForeignKey('products.id'))
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
       
    def __repr__(self):
        return f'Branch(id={self.id},'+\
            f'Name={self.branch_name})'
                    
    
