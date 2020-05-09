#  List of tuples

items = [('aa', 33, 100.23), ('bb', 34, 98.2), ('aa', 33, 100.23)]

newitems = set(items) # eliminates duplicates
print(newitems)   # {('bb', 34, 98.2), ('aa', 33, 100.23)}

# Dictionary in Dictionary

sharePrices = {
  'aftek': {'curr': 52, 'high': 99, 'low': 22},
  'hdfc': {'curr': 252, 'high': 399, 'low': 122},
  'icici': {'curr': 45, 'high': 85, 'low': 2}  
} 

print(sharePrices['hdfc'])