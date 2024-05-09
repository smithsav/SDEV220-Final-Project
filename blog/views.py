from django.shortcuts import render , redirect
from .forms import ProductForm
from .inventory import Inventory
from .models import product
from django.http import HttpResponseRedirect
from .forms import customer
from django.http import HttpResponse

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
            return redirect('add_product')
        except KeyError:
            # Handle missing fields
            return HttpResponse("Missing required fields. Please fill in all fields.")

    products = product.objects.all()
    return render(request, 'blog/add_products.html', {'products': products})

def view_inventory(request):
    products = product.objects.all()  
    return render(request, 'blog/view_inventory.html', {'products': products})

def record_sale(request):
    if request.method == "POST": 
        form = record_sale(request.POST)
        
        if form.is_valid():
            return HttpResponseRedirect("/record_sale/")

    else:
        form = record_sale()
    return render(request, 'blog/record_sale.html', {"form": form})

def customer(request):
    
    if request.method == "POST":
        form = customer(request.POST)
        
        if form.is_valid():
            return HttpResponseRedirect("/customer/")

    else:
        form = customer()

        return render(request, 'blog/customer.html', {"form": form})
