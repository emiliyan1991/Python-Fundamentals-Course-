number = int(input())
for n in range(1, number + 1):
    total_sum = 0
    working_number = n
    while working_number > 0:
        total_sum += working_number % 10
        working_number = int(working_number / 10)
    if total_sum == 5 or total_sum == 7 or total_sum == 11:
        print(f"{n} -> True")
    else:
        print(f"{n} -> False")