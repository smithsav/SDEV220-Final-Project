from django import forms
from .models import Product


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'price']

def view_inventory(request):
    products = Product.objects.all()
    return render(request, 'view_inventory.html', {'products': products})
