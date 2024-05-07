from django.shortcuts import render , redirect
from django.utils import timezone
from .products import Products
from .forms import ProductForm
from .models import Product
from .inventory import Inventory 
from .forms import PostForm

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_product')  
    else:
        form = ProductForm()

    products = Product.objects.all()

    return render(request, 'add_products.html', {'form': form, 'products': products})

def view_inventory(request):
    products = Product.objects.all()  
    return render(request, 'view_inventory.html', {'products': products})

def record_sale(request):
    return render(request, 'blog/record_sale.html', {})

def add_customerID(request):
    return render(request, 'blog/add_customerID.html', {})
