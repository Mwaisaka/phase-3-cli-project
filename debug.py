#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Product,Supplier, Branch


if __name__ == '__main__':
    
    engine = create_engine('sqlite:///inventory.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb;ipdb.set_trace()

    
    