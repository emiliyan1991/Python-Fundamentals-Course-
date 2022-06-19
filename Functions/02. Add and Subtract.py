def sum_numbers(n1, n2):
    return n1 + n2


def subtract(current_sum, n3):
    return current_sum - n3


n1, n2, n3 = int(input()), int(input()), int(input())
result = subtract(sum_numbers(n1, n2), n3)
print(result)




