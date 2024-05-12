from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
import sqlite3

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
    
    class Meta:
        db_table = 'post'
    
class product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        db_table = 'product'

# Define a function to populate the database from the text file
def populate_database_from_file(file_path):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    with open(file_path, 'r') as file:
        for line in file:
            first_name, last_name = line.strip().split()
            address = "Address"  # Placeholder for now
            phone_number = "Phone Number"  # Placeholder for now
            # Insert the customer into the database
            cursor.execute("INSERT INTO customer (first_name, last_name, address, phone_number) VALUES (?, ?, ?, ?)",
                           (first_name, last_name, address, phone_number))
    conn.commit()
    conn.close()

# Define a function to search for customers in the database
def search_customers_in_database(search_query):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer WHERE first_name LIKE ? OR last_name LIKE ?", ('%' + search_query + '%', '%' + search_query + '%'))
    found_customers = cursor.fetchall()
    conn.close()
    return found_customers

# Example usage
file_path = 'blog/customername.txt' 
search_query = input("Enter search query: ")

# Populate the database (only do this once, or whenever the text file is updated)
populate_database_from_file(file_path)

# Search for customers in the database
found_customers = search_customers_in_database(search_query)
for customer in found_customers:
    print(f"{customer[1]} {customer[2]} - {customer[3]} - {customer[4]}")

class RecordSale(models.Model):
    product_quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sale Record - Quantity: {self.product_quantity}, Total: {self.total}"
    
    class Meta:
        db_table = "record_sale"
