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
import os
from .searchcustomer import search_customer_in_file 


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
    else:
        form = RecordSaleForm()

    record_sales = RecordSale.objects.all()
    
    return render(request, 'blog/record_sale.html', {'form': form, 'record_sales': record_sales})

# def customer_view(request):
#     if request.method == 'POST':
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             customer_details = search_customer_in_file(first_name, last_name)
#             if customer_details:
#                 return render(request, 'blog/customer.html', {'form': form, 'customer_details': customer_details})
#             else:
#                 return render(request, 'blog/customer.html', {'form': form, 'error_message': 'Customer not found.'})
#     else:
#         form = CustomerForm()
#     return render(request, 'blog/customer.html', {'form': form}) # Adjust template path

def customer_view(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            customer_details = search_customer_in_file(first_name, last_name)
            if customer_details:
                found_customers = [customer_details]
            else:
                found_customers = []
            return render(request, 'blog/customer.html', {'form': form, 'found_customers': found_customers})
    else:
        form = CustomerForm()
    return render(request, 'blog/customer.html', {'form': form})