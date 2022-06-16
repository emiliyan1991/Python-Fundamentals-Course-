numbers = input().split(" ")
filtered_list = list()
for number in numbers:
    current_number = abs(float(number))
    filtered_list.append(current_number)
print(filtered_list)
