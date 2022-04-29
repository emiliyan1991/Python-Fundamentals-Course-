nums = (" ").join   input()
new_list = []
zeroes = []
for num in nums:
    current_num = int(num)
    if current_num != 0:
        new_list.append(current_num)
    else:
        zeroes.append(current_num)

for zero in zeroes:
    new_list.append(zero)

print(new_list)



