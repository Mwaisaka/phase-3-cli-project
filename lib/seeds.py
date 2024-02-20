from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Product,Supplier, Branch, Base
from products_list import product_names

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///inventory.db')
    Base.metadata.create_all(engine) 
    Session = sessionmaker(bind=engine)
    session = Session()
    
    session.query(Product).delete()
    session.query(Supplier).delete()
    session.query(Branch).delete()
    
    fake=Faker()
        
    # Use a set to ensure unique cities
    branch_set = set()
    while len(branch_set) < 10:
        branch_set.add(fake.city())
    
    # Convert set to list
    branch_list = list(branch_set)
    
        
    products =[]
    for i in range(50):
        product=Product(
            name=random.choice(product_names),
            item_quantity=random.randint(0,100),
            price=random.randint(100,1000)
        )
        
        session.add(product)
        session.commit()
        
        products.append(product)
    
    suppliers=[]
    for i in range(10):
        supplier=Supplier(
            name=fake.name(),
        )
        session.add(supplier)
        session.commit()
        
        suppliers.append(supplier)
                
    branches=[]
    # Ensure only 10 branches are created
    for _ in range(10):
        product = random.choice(products)
        supplier = random.choice(suppliers)
        
        if product not in supplier.products:
            supplier.products.append(product)
            session.add(supplier)
            session.commit()
            
        branch = Branch(
            branch_name=random.choice(branch_list),
            product_id=product.id,
            supplier_id=supplier.id,
        )
        
        branches.append(branch)
        
    session.bulk_save_objects(branches)
    session.commit()
    session.close()
    
  