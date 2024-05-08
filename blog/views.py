from django.shortcuts import render , redirect
from .forms import ProductForm
from .models import Product
from .inventory import Inventory 

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        price = request.POST['price']
        product = Product.objects.create(name=name, quantity=quantity, price=price)
        product.save()
        return redirect('add_product')

    products = Product.objects.all()
    return render(request, 'add_products.html', {'products': products})

def view_inventory(request):
    products = Product.objects.all()  
    return render(request, 'view_inventory.html', {'products': products})

def record_sale(request):
    return render(request, 'blog/record_sale.html', {})

def customer(request):
    return render(request, 'blog/customer.html', {})
