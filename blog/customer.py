from .forms import CustomerForm  
from .models import Customer     


def customer(file_path):
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