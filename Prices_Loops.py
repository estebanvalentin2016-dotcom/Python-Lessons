prices = [25, 60, 80, 15]
running_total = 0

for price in prices:
    discount = 0
    if price >= 50:
        discount = price * .10
    final_price = price - discount
    running_total += final_price
    print("Price: ", final_price)

print("Running total: ", running_total)