numbers =input()
list_numbers = list(numbers.split(" "))

string = input()
string_list = list(string)
message = []
current_number = 0
Sum = 0
for number in numbers:
    current_number = number.split()
    for i in current_number:
        current = int(i)
        Sum += current
        if Sum > len(string):
            Sum -= len(string)
        continue
    message.append(string[Sum])
    string_list.remove(string[Sum])









