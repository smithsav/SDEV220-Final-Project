from .forms import CustomerForm  
from .models import Customer     
import os
import django

class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        

def read_customers_from_file(file_path):
    customers = []
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if len(data) == 4:
                first_name, last_name = data
                customers.append(Customer(first_name, last_name))
    return customers

def search_customers(customers, search_query):
    found_customers = []
    for customer in customers:
        if search_query.lower() in customer.first_name.lower() or search_query.lower() in customer.last_name.lower():
            found_customers.append(customer)  # Append the individual customer, not the entire list
    return found_customers

# Example usage
file_path = '/blog/customername.txt'
search_query = input("Enter search query: ")
customers = read_customers_from_file(file_path)
found_customers = search_customers(customers, search_query)
for customer in found_customers:
    print(f"{customer.first_name} {customer.last_name}")