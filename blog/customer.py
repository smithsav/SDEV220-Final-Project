
class customer():
    def __init__(self):
        self.customerFName = None
        self.customerLName = None
        self.customerAddress = None
        self.customerNumber = None
          
    def customer_details(self, customerFName, customerLName, customerAddress, customerNumber, customerpayment, customerID):
        self.customerFName = customerFName
        self.customerLName = customerLName
        self.customerAddress = customerAddress
        self.customerNumber = customerNumber
                
    def remove_customer(self, customerID):
        self.removecusmter = customer
    
    def main(self):
        customerFName = input("First Name:", customerFName)
        customerLName = input("Last Name: ", customerLName)
        customerAddress = input ("Address(City, State, Zip code): ", customerAddress)
        customerNumber = int(input("Phone Number(xxx-xxx-xxxx): ", customerNumber))
      

    main()  