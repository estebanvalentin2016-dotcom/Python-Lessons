daily_sales = [120, 75, 200, 40, 150]
qualifying_sale_count = 0
total_sales = 0

for sales in daily_sales:
    if sales >= 100:
        qualifying_sale_count += 1

    total_sales += sales

print("qualifying_sales: ", qualifying_sale_count)
print("total_sales: ", total_sales)