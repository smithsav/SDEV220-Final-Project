from django.shortcuts import render , redirect
from .products import Products
from .forms import AddProductForm
from .models import Product
from .inventory import Inventory 

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('view_inventory')  
    else:
        form = AddProductForm()
    
    return render(request, 'add_product.html', {'form': form})

def view_inventory(request):
    products = Product.objects.all()  
    return render(request, 'view_inventory.html', {'products': products})

def record_sale(request):
    return render(request, 'blog/record_sale.html', {})

def add_customerID(request):
    return render(request, 'blog/add_customerID.html', {})
