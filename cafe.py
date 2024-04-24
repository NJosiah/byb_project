menu = ['tea', 'crossaint', 'muffin', 'juice']
stock = {'tea': 30, 
         'crossaint': 40, 
         'muffin': 35, 
         'juice': 25}

price = {'tea': 2.50,
         'crossaint' : 3.50,
         'muffin': 3.00, 
         'juice': 2.00}

print(stock.values())
print(price.values())

total = 0
for i in menu:
    stock_total = (stock[i]) * (price[i])
    total += stock_total

total_stock = {key: price[key] * stock.get(key, 0)
               for key in price.keys()}

print(total_stock)

print(f"The total of the stock is ${total:.2f}")
      