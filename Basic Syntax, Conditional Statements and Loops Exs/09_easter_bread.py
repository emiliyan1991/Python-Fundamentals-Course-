budget = float(input())
flour_price = float(input())
egg_price = 0.75 * flour_price
liter_milk_price = 1.25 * flour_price
loaf_cost = flour_price + egg_price + (0.25 * liter_milk_price)
bread_counter = 0
colored_egg_counter = 0
total_cost = 0
budget_left = budget
while budget_left >= loaf_cost:
    bread_counter += 1
    colored_egg_counter += 3
    if bread_counter % 3 == 0:
        colored_egg_counter -= bread_counter - 2
    budget_left -= loaf_cost
    total_cost += loaf_cost
diff = (budget - total_cost)
print(f"You made {bread_counter} loaves of Easter bread! Now you have {colored_egg_counter} eggs and "
        f"{diff:.2f}BGN left.")

