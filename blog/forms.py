from django import forms
from .models import product, Customer
from django.shortcuts import render , redirect



class ProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name', 'quantity', 'price']

def view_inventory(request):
    products = product.objects.all()
    return render(request, 'view_inventory.html', {'products': products})

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'address', 'phone_number']

class TotalSalesForm(forms.Form):
    product_quantity = forms.IntegerField(label='Product Quantity')
    subtotal = forms.DecimalField(label='Subtotal')
    tax = forms.DecimalField(label='Tax')
    operation = forms.ChoiceField(choices=(('+', 'Add'), ('-', 'Subtract')), label='Operation')
