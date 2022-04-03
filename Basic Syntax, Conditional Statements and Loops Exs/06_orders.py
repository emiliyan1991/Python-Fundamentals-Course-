number_of_orders = int(input())
total_price = 0
price_for_the_order = 0
for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_count = int(input())
    price_for_the_order = price_per_capsule * days * capsule_count
    print(f"The price for the coffee is: ${price_for_the_order:.2f}")
    total_price += price_for_the_order
    price_for_the_order = 0
print(f"Total: ${total_price:.2f}")

