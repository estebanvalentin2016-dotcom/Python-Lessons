base_pay = 500
sales = 500
customer_rating = 4.0
bonus = 0

if sales >= 1000 and customer_rating >= 4.5:
    bonus = sales * .15
elif sales >= 500 and customer_rating >= 4.0:
    bonus = sales *.05

total_pay = base_pay + bonus
print(total_pay)