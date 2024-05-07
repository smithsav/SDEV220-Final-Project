from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_quantity = models.IntegerField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

class Customer(models.Model):
    customerFname = models.TextField(blank=True, null=True)
    customerLname = models.TextField(blank=True, null=True)
    sutomerAddress = models.TextField(blank=True, null=True)
    customerNumber = models.IntegerField(max_digit=10)

class totalsales(models.Model):
    product_quantity = models.ForeignObject(Product, null=True, on_delete=models.SET_NULL)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    toal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def calculate(self, save=False):
        if not self.product:
            return{}
        subtotal = self.product.price 
        tax_rate = .07
        tax_total = subtotal * tax_rate
        tax_total = float("%.2f" %(tax_total))     
        totalsales= price + tax_total
        totalsales = float ("%.2f" %(totalsales))
        totals = {
            "subtotal": subtotal,
            "tax": tax_total,
            "totalsales": totalsales,
            }  
        
        for k,v in totals.items():
            setattr(self, k, v)
            if save==True:
                self.save()
        return totals