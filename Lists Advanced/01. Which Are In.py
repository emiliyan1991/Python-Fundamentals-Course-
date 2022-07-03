string_1 = list(input().split(", "))
string_2 = input()

filter_list = list(text for text in string_1  if text in string_2 )
print(filter_list)