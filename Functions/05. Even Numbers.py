def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


result = filter(check_even, list(map(int, input().split(" "))))
print(list(result))
