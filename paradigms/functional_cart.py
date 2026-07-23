from functools import reduce

products = [

    {"name": "Rice", "unit_price": 12000, "quantity": 2},
     {"name": "Oil", "unit_price": 8000, "quantity": 1},
     {"name": "Sugar", "unit_price": 5000, "quantity": 3}
]

def calculate_product_price(product):
    return product["unit_price"] * product["quantity"]

prices = list(map(calculate_product_price,products))

total = reduce (lambda x, y: x+y, prices)

def apply_discount(total):
    return total * 0.9 if total > 50000 else total

final_price = apply_discount(total)

print("Final price: ",
final_price, "FCFA")