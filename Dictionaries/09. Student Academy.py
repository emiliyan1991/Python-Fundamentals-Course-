n = int(input())
my_dict = {}
for i in range(n):
    student = input()
    grade = float(input())
    if student not in my_dict:
        my_dict[student] = []
    my_dict[student].append(float(grade))

for key, value in my_dict.items():
    average = sum(my_dict[key]) / len(my_dict[key])
    if average >= 4.5:

        print(f"{key} -> {average:.2f}")
