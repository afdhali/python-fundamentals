# {value:flags} only works with template literals

price1 = 13.25
price2 = 15.4
price3 = -10.55

print(f"Price 1 is ${price1:10.2f}")
print(f"Price 2 is ${price2:10.2f}")
print(f"Price 3 is ${price3:10.2f}")
