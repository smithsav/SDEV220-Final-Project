class Products:
    def __init__(self):
        self.productDetails = {}  # Dictionary to store product details {productName: [productQuantity, productPrice]}

    def add_product(self, productName, productQuantity, productPrice):
        if productName in self.productDetails:
            print("Product already exists. Use update_product() to update details.")
        else:
            self.productDetails[productName] = [productQuantity, productPrice]
            print(f"{productName} added successfully.")

    def remove_product(self, productName):
        if productName in self.productDetails:
            del self.productDetails[productName]
            print(f"{productName} removed successfully.")
        else:
            print("Product not found.")

    def update_product(self, productName, productQuantity=None, productPrice=None):
        if productName in self.productDetails:
            if productQuantity is not None:
                self.productDetails[productName][0] = productQuantity
            if productPrice is not None:
                self.productDetails[productName][1] = productPrice
            print(f"{productName} updated successfully.")
        else:
            print("Product not found.")

    def order_product(self, productName, quantity):
        if productName in self.productDetails:
            available_quantity = self.productDetails[productName][0]
            if available_quantity >= quantity:
                print(f"{quantity} {productName}(s) ordered successfully.")
                self.productDetails[productName][0] -= quantity
            else:
                print(f"Insufficient stock. Only {available_quantity} {productName}(s) available.")
        else:
            print("Product not found.")

    def product_detail(self, productName):
        if productName in self.productDetails:
            quantity, price = self.productDetails[productName]
            print(f"Product Name: {productName}")
            print(f"Quantity: {quantity}")
            print(f"Price: {price}")
        else:
            print("Product not found.")
