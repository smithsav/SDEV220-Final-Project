from django.shortcuts import render , redirect
from .forms import ProductForm
from .inventory import Inventory
from .models import product
from django.http import HttpResponseRedirect
from .forms import CustomerForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Customer
from django.shortcuts import render
from .forms import RecordSaleForm
from .totalsales import calculate_totalsales
from .models import RecordSale


def base(request):
    return render(request, 'blog/base.html')

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def add_product(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            quantity = request.POST['quantity']
            price = request.POST['price']
            new_product = product.objects.create(name=name, quantity=quantity, price=price)
            new_product.save()
            return redirect('add_products')
        except KeyError:
            # Handle missing fields
            return HttpResponse("Missing required fields. Please fill in all fields.")

    products = product.objects.all()
    return render(request, 'blog/add_products.html', {'products': products})

def view_inventory(request):
    products = product.objects.all()  
    return render(request, 'blog/view_inventory.html', {'products': products})

def record_sale(request):
    if request.method == 'POST':
        form = RecordSaleForm(request.POST)
        if form.is_valid():
            product_quantity = form.cleaned_data['product_quantity']
            subtotal = form.cleaned_data['subtotal']
            tax = form.cleaned_data['tax']
            operation = form.cleaned_data['operation']
            total_sales = calculate_totalsales(product_quantity, subtotal, tax, operation)
            record_sale = RecordSale.objects.create(
                product_quantity=product_quantity,
                subtotal=subtotal,
                tax=tax,
                total=total_sales
            )
            return redirect('record_sale')
        # If form is not valid, render the form again with validation errors
    else:
        form = RecordSaleForm()
    return render(request, 'blog/record_sale.html', {'form': form})

def customer(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '') 
        first_name = request.POST.get('first_name', '') 
        last_name = request.POST.get('last_name', '') 
        
        found_customers = []
        with open('customername.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                file_first_name, file_last_name, address, phone_number = data
                
                if (first_name.lower() in file_first_name.lower() or
                    last_name.lower() in file_last_name.lower()):
                    
                    found_customers.append({
                        'first_name': file_first_name,
                        'last_name': file_last_name,
                        'address': address,
                        'phone_number': phone_number
                    })
        
        return render(request, 'customer.html', {
            'found_customers': found_customers,
            'search_query': search_query,
            'first_name': first_name,
            'last_name': last_name
        })
    else:
        return render(request, 'blog/customer.html')