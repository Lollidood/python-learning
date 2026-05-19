# Task: Calculate the cost of selected burger ingredients using ChainMap + Counter
# https://github.com/python-generation/Professional/tree/main/Module_6/Module_6.9/Module_6.9.23

from collections import ChainMap
from collections import Counter

# Dictionaries with ingredient prices
bread = {'sesame bun': 15, 'plain bun': 10, 'rye bun': 15}
meat = {'chicken patty': 50, 'beef patty': 70, 'fish patty': 40}
sauce = {'garlic cream': 15, 'ketchup': 10, 'mustard': 10, 'barbecue': 15, 'chili': 15}
vegetables = {'onion': 10, 'lettuce': 15, 'tomato': 15, 'cucumbers': 10}
toppings = {'cheese': 25, 'egg': 15, 'bacon': 30}

# Merge all dictionaries into one (for easy price lookup by ingredient)
burger = ChainMap(bread, meat, sauce, vegetables, toppings)

# User input of ingredients (comma-separated)
ingr = input().split(',')

# Count how many times each ingredient appears
count = Counter(ingr)

# Maximum length of ingredient name (for aligning output)
maxi = max(map(len, ingr))

# Variables for total price and table width
total_price = 0
line_len = 0

# Output ingredients in alphabetical order and calculate cost
for item in sorted(count):
    line = f'{item:<{maxi}} x {count[item]}'
    total_price += burger[item] * count[item]

    # Calculate the maximum line width for formatting
    if len(line) > line_len:
        line_len = len(line)

    print(line)

# Total line
result_line = f'TOTAL: {total_price} rubles'
