def calculate_totalsales(product_quantity, subtotal, tax, operation):
    if operation == '+':
        total_sales = subtotal + tax
    else:
        total_sales = subtotal - tax
    
    
    total_sales *= product_quantity
    
    return total_sales