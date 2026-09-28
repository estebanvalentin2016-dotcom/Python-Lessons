order_amounts = [35, 60, 20, 85, 50]
total_delivery_fees = 0
free_delivery_count = 0

for orders in order_amounts:
    delivery_fee = 0
    if orders < 50:
        delivery_fee = 6
    else:
        free_delivery_count += 1

    total_delivery_fees += delivery_fee

print("Free delivery fees: ", free_delivery_count)
print("Total delivery fees: ", total_delivery_fees)