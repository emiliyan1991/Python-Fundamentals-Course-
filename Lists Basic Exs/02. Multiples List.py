factor = int(input())
count = int(input())
new_list = []
for i in range(1, count + 1):
    current_num = i
    new_list.append(current_num * factor)
print(new_list)
