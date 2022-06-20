def sum_of_digits(number):
    odd_sum = 0
    even_sum = 0
    for i in range(len(number)):
        current_digit = int(number[i])
        if current_digit % 2 == 0:
            even_sum += current_digit
        else:
            odd_sum += current_digit
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


number = input()
sum_of_digits(number)
