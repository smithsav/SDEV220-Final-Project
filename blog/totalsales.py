class totalsales:
    def __init__(self):
        self.totalsales = None
    
    def calculate_totalsales(self, monday, tuesday, wednesday, thursday, friday, price_per_unit):
        self.totalsales = (monday + tuesday + wednesday + thursday + friday) * price_per_unit
    
def main():
    # Assuming the price per unit is constant for all products
    price_per_unit = float(input("Enter the price per unit of the product: "))
    
    monday = int(input("Enter the product quantity for Monday: "))
    tuesday = int(input("Enter the product quantity for Tuesday: "))
    wednesday = int(input("Enter the product quantity for Wednesday: "))
    thursday = int(input("Enter the product quantity for Thursday: "))
    friday = int(input("Enter the product quantity for Friday: "))    
    
    total_sales_obj = totalsales()
    total_sales_obj.calculate_totalsales(monday, tuesday, wednesday, thursday, friday, price_per_unit)
    
    print("Total sales for the week are: ", total_sales_obj.totalsales)

if __name__ == "__main__":
    main()