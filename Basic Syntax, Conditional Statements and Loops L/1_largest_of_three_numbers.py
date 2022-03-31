import sys
first_num = int(input())
second_num = int(input())
third_num = int(input())
biggest_number = - sys.maxsize
if first_num > biggest_number:
    biggest_number = first_num
if second_num > biggest_number:
    biggest_number = second_num
if third_num > biggest_number:
    biggest_number = third_num
print(biggest_number)
