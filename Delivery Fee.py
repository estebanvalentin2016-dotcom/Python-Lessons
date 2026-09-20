order_total = 100
delivery_fee = 10

if order_total >= 100:
    delivery_fee = 0
elif order_total >= 50:
    delivery_fee = 5

final_total = order_total + delivery_fee
print(final_total)
