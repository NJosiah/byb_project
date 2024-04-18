menu = ['tea', 'crossaint', 'full english', 'orange juice']
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

total_stock = {key: price[key] * stock.get(key, 0)
               for key in price.keys()}
    
print(total_stock)
    