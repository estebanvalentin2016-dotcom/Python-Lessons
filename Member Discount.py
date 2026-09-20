order_total = 100
is_member = True
discount = 0

if is_member == True and order_total >= 100:
    discount = order_total * .20
elif is_member == True and order_total < 100:
    discount = order_total * .10

final_total = order_total - discount
print(final_total)