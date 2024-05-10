from django.shortcuts import render , redirect
from .forms import ProductForm
from .inventory import Inventory
from .models import product
from django.http import HttpResponseRedirect
from .forms import CustomerForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def base(request):
    return render(request, 'blog/base.html')

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def product_list(request):
    products = product.objects.all()
    return render(request, 'blog/product_list.html', {'products': products})

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

def delete_product(request, product_id):
    # Retrieve the product instance or return a 404 error if not found
    product_instance = get_object_or_404(product, pk=product_id)
    
    # Delete the product
    product_instance.delete()
    
    # Redirect to the view_inventory page after deletion
    return redirect('view_inventory')

def update_product(request, product_id):
    # Retrieve the product instance or return a 404 error if not found
    product_instance = get_object_or_404(product, pk=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product_instance)
        if form.is_valid():
            form.save()
            return redirect('view_inventory')
    else:
        form = ProductForm(instance=product_instance)
    
    return render(request, 'blog/update_product.html', {'form': form})

def view_inventory(request):
    products = product.objects.all()  
    return render(request, 'blog/view_inventory.html', {'products': products})

def record_sale(request):
    return render(request, 'blog/record_sale.html', {})

def customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        
        if form.is_valid():
                return render(request, 'blog/customer.html', {"form": form, "success_message": "Form submitted successfully!"})

    else:
        form = CustomerForm()

    return render(request, 'blog/customer.html', {"form": form})
