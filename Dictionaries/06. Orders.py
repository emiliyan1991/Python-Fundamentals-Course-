command = input()
product_dict = dict()
while command != "buy":
    cmd = command.split(" ")
    product = cmd[0]
    price = float(cmd[1])
    quantity = int(cmd[2])
    if product not in product_dict:
        product_dict[product] = [price, quantity]
    else:
        product_dict[product] = [price, quantity+product_dict[product][1]]

    command = input()
for key,value in product_dict.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")








