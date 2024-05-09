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

def update_product(request, product_id):
    product = product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            price = form.cleaned_data['price']
            Inventory.update_product(product_id, name, quantity, price)
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form, 'product_id': product_id})

def delete_product(request, product_id):
    if request.method == 'POST':
        Inventory.delete_product(product_id)
        return redirect('product_list')
    else:
        product = product.objects.get(pk=product_id)
        return render(request, 'delete_product.html', {'product': product})

def product_list(request):
    products = product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def record_sale(request):
    return render(request, 'blog/record_sale.html', {})

def customer(request):
    
    if request.method == "POST":
        form = customer(request.POST)
        
        if form.is_valid():
            return HttpResponseRedirect("/customer/")

    else:
        form = customer()

        return render(request, 'blog/customer.html', {"form": form})
