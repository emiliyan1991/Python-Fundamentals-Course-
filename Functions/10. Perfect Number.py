def perfection_check(number):
    is_perfect_number = False
    new_list = []
    for i in range(1, number):
        current_divisor = i
        if number % current_divisor == 0:
            new_list.append(current_divisor)
        if sum(new_list) == number:
            is_perfect_number = True
    if is_perfect_number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())
perfection_check(number)

