emp_dict = {}
text = input()
while text != "End":
    info = text.split(" -> ")
    firm = info[0]
    worker = info[1]
    if firm not in emp_dict:
        emp_dict[firm] = []
    if worker not in emp_dict[firm]:
        emp_dict[firm].append(worker)

    text = input()

for key, value in emp_dict.items():
    print(key)
    for i in value:
        print(f"-- {i}")