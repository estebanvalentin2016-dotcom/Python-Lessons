order_total = 35

if order_total >= 50:
    print("Free shipping")
elif order_total >= 25 and order_total < 50:
    print("Shipping costs $5")
else:
    print("Shipping costs $10")