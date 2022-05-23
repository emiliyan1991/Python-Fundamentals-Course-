items = {}
item = input()

while item != "stop":
    quantity = int(input())
    if item not in items:
        items[item] = quantity
    else:
        items[item] += quantity
    item = input()

for key, value in items.items():
    print(f"{key} -> {value}")
