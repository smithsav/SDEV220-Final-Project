from django import forms
from .models import Product
from django.shortcuts import render , redirect
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_quantity', 'product_price']

def view_inventory(request):
    products = Product.objects.all()
    return render(request, 'view_inventory.html', {'products': products})
