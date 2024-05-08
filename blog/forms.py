from django import forms
from .models import product
from django.shortcuts import render , redirect
import calculation

class ProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name', 'quantity', 'price']

def view_inventory(request):
    products = product.objects.all()
    return render(request, 'view_inventory.html', {'products': products})

class customer(forms.Form):
    customerFname = forms.CharField(max_length = 200)
    customerLname = forms.CharField(max_length = 200)
    customerAddress = forms.CharField()
    customerNumber = forms.IntegerField()

class totalsales(forms.Form):
    quantity = forms.DecimalField()
    price = forms.DecimalField()
    amount = forms.DecimalField(
        widget=calculation.FormulaInput('quantity*price')
    )
    apply_taxes = forms.BooleanField(initial=True)
    tax = forms.DecimalField(
        widget=calculation.FormulaInput('apply_taxes ? parseFloat(amount/11).toFixed(2) : 0.0') 
    )
