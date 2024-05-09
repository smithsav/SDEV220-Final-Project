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
    
    