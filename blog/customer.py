
from .forms import CustomerForm  
from .models import Customer     
class Customer:
    def __init__(self):
        self.customerFName = None
        self.customerLName = None
        self.customerAddress = None
        self.customerNumber = None
          
    def customer_details(self, customerFName, customerLName, customerAddress, customerNumber):
        self.customerFName = customerFName
        self.customerLName = customerLName
        self.customerAddress = customerAddress
        self.customerNumber = customerNumber
                
    def remove_customer(self, customer):
        self.removecustomer = customer
    
    def search_customer(self, search_name):
        customer_names = open(r"customername.txt", "r").readlines()
        line = 1
        found = False
        for customerFname in customer_names:
            if customerFname.strip() == search_name:
                found = True
                print(f"Customer: {customerFname.strip()} \nLine No. {line + 1}")
                break
            line += 1
        if not found:
            print("No Customer Found, Please Try Again")