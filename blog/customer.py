
class customer():
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
        self.removecusmter = customer
    
    def main():
        line = 1

    customernames = open(r"customername.txt", "r")
    customername = customernames.readlines()

    searchcustomername = input("Please enter the name you want to find: ")
    for customerFname in customername:
        if customerFname == searchcustomername:
            line = line + 1
            print(f"Customer: {customerFname} \nLine No. {line + 1}")
          
        else:
            print("No Customer Found, Please Try Again")
    
    

    main()  