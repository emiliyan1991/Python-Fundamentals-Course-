number_of_lines = int(input())
liters_in = 0
is_tank_full = False
for i in range(number_of_lines):
    quantity_poured = int(input())
    liters_in += quantity_poured
    if liters_in > 255:
        print("Insufficient capacity!")
        liters_in -= quantity_poured

print(liters_in)
