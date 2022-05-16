fires = input().split("#")
water_quantity = int(input())
total_effort = 0
total_fire = 0
condition = False
print("Cells:")
for i in fires:
    current_fire = i.split(" = ")
    current_fire_type = current_fire[0]
    current_fire_value = int(current_fire[1])
    condition = False
    if current_fire_type == "High":
        if 81 <= current_fire_value <= 125:
            condition = True
    elif current_fire_type == "Medium":
        if 51 <= current_fire_value <= 80:
            condition = True
    elif current_fire_type == "Low":
        if 1 <= current_fire_value <= 50:
            condition = True
    if condition:
        if water_quantity >= current_fire_value:
            water_quantity -= current_fire_value
            total_fire += current_fire_value
            total_effort += 0.25 * current_fire_value
            print(f" - {current_fire_value}")
print(f'Effort: {total_effort:.2f}')
print(f"Total Fire: {total_fire}")

