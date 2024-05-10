class Inventory:
    def __init__(self):
        self.__inventoryType = {}  

    def inventory_types(self):
        
        return list(self.__inventoryType.keys())

    def inventory_quantities(self):
       
        return list(self.__inventoryType.values())

    def inventory_price(self, inventory_type):
        
        if inventory_type in self.__inventoryType:
            return self.__inventoryType[inventory_type][1]
        else:
            raise KeyError("Inventory type not found.")

    def order_amount(self, inventory_type, quantity):
        
        if inventory_type in self.__inventoryType:
            available_quantity, price_per_unit = self.__inventoryType[inventory_type]
            if available_quantity >= quantity:
                total_price = price_per_unit * quantity
                print(f"Order placed for {quantity} units of {inventory_type}. Total amount: ${total_price}")
                self.__inventoryType[inventory_type][0] -= quantity
            else:
                print(f"Insufficient stock. Only {available_quantity} units of {inventory_type} available.")
        else:
            raise KeyError("Inventory type not found.")