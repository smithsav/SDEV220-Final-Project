from django.shortcuts import render
from .products import Products  
from .forms import AddProductForm
from .models import Product

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def add_product(request):
    if request.method == 'POST':
        print(request.POST)  
        form = AddProductForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            product_quantity = form.cleaned_data['product_quantity']
            product_price = form.cleaned_data['product_price']
            
            products_manager = Products()
            
            products_manager.add_product(product_name, product_quantity, product_price)
            
            return render(request, 'add_products.html', {'form': form, 'product': {'name': product_name, 'quantity': product_quantity, 'price': product_price}})
    else:
        form = AddProductForm()
    
    return render(request, 'blog/add_products.html', {})

def view_inventory(request):
    products = Product.objects.all()

    return render(request, 'view_inventory.html', {'products': products})

def record_sale(request):
    return render(request, 'blog/record_sale.html', {})

def add_customerID(request):
    return render(request, 'blog/add_customerID.html', {})
