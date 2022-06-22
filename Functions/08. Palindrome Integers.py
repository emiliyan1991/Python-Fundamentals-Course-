def check_palindrome(numbers):
    new_list = numbers.split(", ")
    for num in new_list:
        if num == num[::-1]:
            print("True")
        else:
            print("False")


numbers = input()
check_palindrome(numbers)
