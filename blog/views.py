from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def add_product(request):
    return render(request, 'blog/add_product.html', {})

def view_inventory(request):
    return render(request, 'blog/view_inventory.html', {})

def record_sale(request):
    return render(request, 'blog/record_sale.html', {})

def add_customerID(request):
    return render(request, 'blog/add_customerID.html', {})
