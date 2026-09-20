order_total = 51
discount = 0

if order_total >= 100:
    discount = order_total * .20
elif order_total >= 50:
    discount = order_total * .10

final_price = order_total - discount
print(final_price)