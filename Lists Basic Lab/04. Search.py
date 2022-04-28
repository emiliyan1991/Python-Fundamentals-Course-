num = int(input())
word = input()
list1 = []
filtered_list = []
for i in range(num):
    current_string = input()
    list1.append(current_string)
print(list1)

for k in range(len(list1)):
    current_element = list1[k]
    if word in current_element:
        filtered_list.append(current_element)
print(filtered_list)
