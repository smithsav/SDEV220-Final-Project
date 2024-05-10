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

class RecordSaleForm(forms.Form):
    product_quantity = forms.IntegerField()
    subtotal = forms.DecimalField(max_digits=10, decimal_places=2)
    tax = forms.DecimalField(max_digits=10, decimal_places=2)
    operation = forms.ChoiceField(choices=(('+', 'Add'), ('-', 'Subtract')))
