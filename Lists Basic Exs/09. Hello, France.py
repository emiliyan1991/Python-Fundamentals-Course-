item_list = input().split("|")
budget = int(input())
current_budget = budget
# print(item_list)
condition = False
income = 0
new_list = []
total_item_cost = 0
for item in item_list:
    current_item = item.split("->")
    item_type = current_item[0]
    item_price = float(current_item[1])
    condition = False

    if item_type == "Clothes":
        if item_price <= 50:
            condition = True
    elif item_type == "Shoes":
        if item_price <= 35:
            condition = True
    if item_type == "Accessories":
        if item_price <= 20.50:
            condition = True

    if condition:
        if item_price <= current_budget:
            current_budget -= item_price
            total_item_cost += item_price
            new_item_price = 1.4 * item_price
            income += new_item_price
            new_list.append(f"{new_item_price:.2f}")

print(" ".join(new_list))


profit = (abs(income - total_item_cost) )
print(f"Profit: {profit:.2f}")
if budget + profit >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

