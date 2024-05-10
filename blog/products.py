class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def order(self, quantity):
        if self.quantity >= quantity:
            print(f"{quantity} {self.name}(s) ordered successfully.")
            self.quantity -= quantity
        else:
            print(f"Insufficient stock. Only {self.quantity} {self.name}(s) available.")

    def update(self, quantity=None, price=None):
        if quantity is not None:
            self.quantity = quantity
        if price is not None:
            self.price = price
        print(f"{self.name} updated successfully.")

    def __str__(self):
        return f"Product Name: {self.name}, Quantity: {self.quantity}, Price: {self.price}"

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, name, quantity, price):
        if name in self.products:
            print("Product already exists. Use update_product() to update details.")
        else:
            self.products[name] = Product(name, quantity, price)
            print(f"{name} added successfully.")

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
            print(f"{name} removed successfully.")
        else:
            print("Product not found.")

    def update_product(self, name, quantity=None, price=None):
        if name in self.products:
            self.products[name].update(quantity, price)
        else:
            print("Product not found.")

    def get_product_detail(self, name):
        if name in self.products:
            print(self.products[name])
        else: