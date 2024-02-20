#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Product,Supplier, Branch,Base

def add_new_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter product quantity: "))
    price = int(input("Enter product price: "))

    new_product = Product()
    new_product.add_new_product(name, quantity, price)

def remove_product():
    name = input("Enter the name of the product to remove: ")
    Product().remove_product(name)

def update_product_price():
    name = input("Enter the name of the product to update: ")
    new_price = int(input("Enter the new price: "))
    
    Product().update_product_price(name, new_price)

def search_product_by_name():
    name = input("Enter the name of the product to search: ")
    Product.search_by_product_name(name)

def show_all_products():
    Product.show_all_products()

if __name__ == '__main__':
      
    engine = create_engine('sqlite:///inventory.db')
    Base.metadata.create_all(engine) 
    Session = sessionmaker(bind=engine)
    session = Session()
6
while True:
    print("\nOptions:")
    print("1. Add a new product")
    print("2. Remove a product")
    print("3. Update a product's price")
    print("4. Search a product by name")
    print("5. Show all products")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_new_product()
    elif choice == '2':
        remove_product()
    elif choice == '3':
        update_product_price()
    elif choice == '4':
        search_product_by_name()
    elif choice == '5':
        show_all_products()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")   


