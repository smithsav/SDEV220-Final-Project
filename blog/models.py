from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

class Customer(models.Model):
    customerFname = models.TextField(blank=True, null=True)
    customerLname = models.TextField(blank=True, null=True)
    sutomerAddress = models.TextField(blank=True, null=True)
    customerNumber = models.IntegerField()     
    
    def __str__(self):
        return self.customer

class Record_sale(models.Model):
    product_quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    toal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.record_sale
    
class Inventory:
    @staticmethod
    def add_product(name, quantity, price):
        product.objects.create(name=name, quantity=quantity, price=price)

    @staticmethod
    def update_product(product_id, name, quantity, price):
        product_instance = product.objects.get(pk=product_id)
        product_instance.name = name
        product_instance.quantity = quantity
        product_instance.price = price
        product_instance.save()

    @staticmethod
    def delete_product(product_id):
        product.objects.get(pk=product_id).delete()
