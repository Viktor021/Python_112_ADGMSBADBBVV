def total_cost(price, tax_rate, discount):
    return price + (price * tax_rate) - discount

price = 100
tax_rate = 0.05
discount = 10
print(total_cost(price, tax_rate, discount))
