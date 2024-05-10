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
            record_sale = RecordSaleForm.objects.create(
                product_quantity=product_quantity,
                subtotal=subtotal,
                tax=tax,
                total=total_sales
            )
            record_sale.save()
            return redirect('record_sale')  #
    else:
        form = RecordSaleForm()
    return render(request, 'record_sale.html', {'form': form})

def customer(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '') 
        found_customers = []
        with open('customername.txt', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                first_name, last_name, address, phone_number = data
                
                if search_query.lower() in first_name.lower() or search_query.lower() in last_name.lower():
                    found_customers.append({
                        'first_name': first_name,
                        'last_name': last_name,
                        'address': address,
                        'phone_number': phone_number
                    })
        first_name = request.POST.get('first_name', '') 
        last_name = request.POST.get('last_name', '') 
        return render(request, 'customer.html', {'found_customers': found_customers, 'search_query': search_query})
    else:
        return render(request, 'customer.html')