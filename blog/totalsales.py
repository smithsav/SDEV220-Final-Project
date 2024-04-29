import products.py

class totalsales():
    def __init__(self):
        self.totalsales = None
        self.totalquantity = None
    
    def total(self, totalsales, totalquantity):
        self.totalsales = totalsales
        self.totalquantity = totalquantity
        

    def main():
        Monday = int(input("Enter the store sales for Monday: "))
        Tuesday = int(input("Enter the store sales for Tuesday: "))
        Wednesday = int(input("Enter the store sales for Wednesday: "))
        Thursday = int(input("Enter the store sales for Thursday: "))
        Friday = int(input("Enter the store sales or Friday: "))    
        
        total = totalsales(Monday, Tuesday, Wednesday, Thursday, Friday)
        print ("Total sales for the week are: ", totalsales)
        
        monday = int(input("Enter the product quantity for Monday: "))
        tuesday = int(input("Enter the product quantity for Tuesday: "))
        wednesday = int(input("Enter the product quantity for Wednesday: "))
        thursday = int(input("Enter the product quantity for Thursday: "))
        friday = int(input("Enter the product qanntity or Friday: "))    
        
        total = totalquantity(monday, tuesday, wednesday, thursday, friday)
        print ("Total qunatities for the week are:", totalquantity)
    
    
    def totalsales(Monday, Tuesday, Wednesday, Thursday, Friday)
        totalperweek = Monday + Tuesday + Wednesday + Thursday + Friday
        return totalperweek
    
    def totalquantity(monday, tuesday, wednesday, thursday, friday)
        totalperweekquantity = monday + tuesday + wednesday + thursday + friday
        return totalperweekquantity
    
    main()