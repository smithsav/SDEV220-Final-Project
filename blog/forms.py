from django import forms

class AddProductForm(forms.Form):
    product_name = forms.CharField(max_length=100)
    product_quantity = forms.IntegerField()
    product_price = forms.DecimalField()