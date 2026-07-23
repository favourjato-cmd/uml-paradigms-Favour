products = [
    {"name": "Rice",
     "unit_price": 12000, "quantity": 2},
     {"name": "Oil", "unit_price": 8000, "quantity": 1},
     {"name": "Sugar",
      "unit_price": 5000, "quantity": 3}
]

total = 0

for product in products:
    total = total +
    (product["unit_price"] *
     product["quantity"])

    if total > 50000:
        total = total * 0.9

        print("Final price:", total,"FCFA")
