stock_levels = [3, 12, 0, 7, 2]
unit_orders = 0

for stock in stock_levels:
    if stock < 5:
       required_stock = 10 - stock
       unit_orders += required_stock
       print("Required stock: ", required_stock)
    else:
       print("No Order")

print("unit_orders: ", unit_orders)
