from .forms import record_sale
from .models import record_sale

class totalsales:
    def __init__(self):
        self.totalsales = None
        self.totalquantity = None
    
    def calculate_totalsales(self, Monday, Tuesday, Wednesday, Thursday, Friday):
        self.totalsales = Monday + Tuesday + Wednesday + Thursday + Friday
    
    def calculate_totalquantity(self, monday, tuesday, wednesday, thursday, friday):
        self.totalquantity = monday + tuesday + wednesday + thursday + friday
        
def main():
    Monday = int(input("Enter the store sales for Monday: "))
    Tuesday = int(input("Enter the store sales for Tuesday: "))
    Wednesday = int(input("Enter the store sales for Wednesday: "))
    Thursday = int(input("Enter the store sales for Thursday: "))
    Friday = int(input("Enter the store sales for Friday: "))    
    
    total_sales_obj = TotalSales()
    total_sales_obj.calculate_totalsales(Monday, Tuesday, Wednesday, Thursday, Friday)
    
    monday = int(input("Enter the product quantity for Monday: "))
    tuesday = int(input("Enter the product quantity for Tuesday: "))
    wednesday = int(input("Enter the product quantity for Wednesday: "))
    thursday = int(input("Enter the product quantity for Thursday: "))
    friday = int(input("Enter the product quantity for Friday: "))    
    
    total_quantity_obj = TotalSales()
    total_quantity_obj.calculate_totalquantity(monday, tuesday, wednesday, thursday, friday)
    
    print ("Total sales for the week are: ", total_sales_obj.totalsales)
    print ("Total quantities for the week are:", total_quantity_obj.totalquantity)

if __name__ == "__main__":
    main()
