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
    
class product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        db_table = 'blog_product'

# class Address(models.Model):
#     CustomerFname = models.CharField(max_length=30)
#     customeraddress = models.CharField(max_length=50)
#     city = models.CharField(max_length=60, default="Miami")
#     state = models.CharField(max_length=30, default="Florida")
#     zipcode = models.CharField(max_length=5, default="33165")
#     country = models.CharField(max_length=50)

#     class Meta:
#         verbose_name = 'Address'
#         verbose_name_plural = 'Address'

#     def __str__(self):
#         return self.name
class customer(models.Model):
    customerFname = models.TextField(blank=True, null=True)
    customerLname = models.TextField(blank=True, null=True)
    sutomerAddress = models.TextField(blank=True, null=True)
    customerNumber = models.IntegerField()     
    
    def __str__(self):
        return self.customer

class record_sale(models.Model):
    product_quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    toal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.record_sale
    
class Inventory:
    def add_product(name, quantity, price):
        product.objects.create(name=name, quantity=quantity, price=price)

    def update_product(product_id, name, quantity, price):
        product = product.objects.get(pk=product_id)
        product.name = name
        product.quantity = quantity
        product.price = price
        product.save()

    def delete_product(product_id):
        product.objects.get(pk=product_id).delete()
