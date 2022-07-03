numbers = input().split(", ")
numbers_list = list(map(int, numbers))
even_numbers = []
for i in range(len(numbers)):
    if numbers_list[i] % 2 == 0:
        even_numbers.append(i)

print(even_numbers)

        