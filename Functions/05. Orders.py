def price_info(product, quantity):
    if product == "water":
        return quantity
    elif product == "coffee":
        return quantity * 1.5
    elif product == "coke":
        return quantity * 1.4
    elif product == "snacks":
        return quantity * 2


result = price_info(product=input(), quantity=int(input()))
print(f"{result:.2f}")

