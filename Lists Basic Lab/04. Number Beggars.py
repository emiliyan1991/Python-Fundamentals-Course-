string = input().split(', ')
beggars = int(input())
outcome = []
sum = 0
for i in range(beggars):
    for j in string:
        current_number = j
        while int(current_number) < len(string):
            sum += string[j]
            j += beggars
    print(sum)







