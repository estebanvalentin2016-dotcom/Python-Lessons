base_pay = 500
customer_rating = 4.8
sales_amounts = [1200, 800, 400]

for sales in sales_amounts:
    bonus = 0
    if sales >= 1000:
        bonus = sales * .15
    elif sales >= 500:
        bonus = sales * .05
    total_pay = base_pay + bonus
    print(total_pay)