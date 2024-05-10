from .forms import CustomerForm  
from .models import Customer     

def main():
    populate_customers_from_file('customername.txt')
    print('Customers populated successfully')
    
def populate_customers_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            first_name, last_name, address, phone_number = data
            Customer.objects.create(
                first_name=first_name,
                last_name=last_name,
                address=address,
                phone_number=phone_number
            )
            
if __name__ == "__main__":
    main()