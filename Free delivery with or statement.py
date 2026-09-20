order_total = 35
is_member = True
delivery_fee = 10

if is_member == True or order_total >= 50:
    delivery_fee = 0
else:
    delivery_fee = 10

final_total = order_total + delivery_fee
print(final_total)
