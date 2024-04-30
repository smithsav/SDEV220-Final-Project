class Products:
    def __init__(self):
        self.product_details = {}  
        
    def add_product(self, product_name, product_quantity, product_price):
        if product_name in self.product_details:
            print("Product already exists. Use update_product() to update details.")
        else:
            self.product_details[product_name] = [product_quantity, product_price]
            print(f"{product_name} added successfully.")

    def remove_product(self, product_name):
        if product_name in self.product_details:
            del self.product_details[product_name]
            print(f"{product_name} removed successfully.")
        else:
            print("Product not found.")

    def update_product(self, product_name, product_quantity=None, product_price=None):
        if product_name in self.product_details:
            if product_quantity is not None:
                self.product_details[product_name][0] = product_quantity
            if product_price is not None:
                self.product_details[product_name][1] = product_price
            print(f"{product_name} updated successfully.")
        else:
            print("Product not found.")

    def order_product(self, product_name, quantity):
        if product_name in self.product_details:
            available_quantity = self.product_details[product_name][0]
            if available_quantity >= quantity:
                print(f"{quantity} {product_name}(s) ordered successfully.")
                self.product_details[product_name][0] -= quantity
            else:
                print(f"Insufficient stock. Only {available_quantity} {product_name}(s) available.")
        else:
            print("Product not found.")

    def product_detail(self, product_name):
        if product_name in self.product_details:
            quantity, price = self.product_details[product_name]
            print(f"Product Name: {product_name}")
            print(f"Quantity: {quantity}")
            print(f"Price: {price}")
        else:
            print("Product not found.")
