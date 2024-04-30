class Inventory:
    def __init__(self):
        self.inventoryType = {}  

    def inventory_type(self):
        return self.inventoryType.keys()

    def inventory_quantity(self):
        return self.inventoryType.values()

    def inventory_price(self, inventoryType):
        if inventoryType in self.inventoryType:
            return self.inventoryType[inventoryType][1]
        else:
            print("Inventory type not found.")

    def order_amount(self, inventoryType, quantity):
        if inventoryType in self.inventoryType:
            available_quantity = self.inventoryType[inventoryType][0]
            price_per_unit = self.inventoryType[inventoryType][1]
            if available_quantity >= quantity:
                total_price = price_per_unit * quantity
                print(f"Order placed for {quantity} units of {inventoryType}. Total amount: ${total_price}")
                self.inventoryType[inventoryType][0] -= quantity
            else:
                print(f"Insufficient stock. Only {available_quantity} units of {inventoryType} available.")
        else:
            print("Inventory type not found.")
