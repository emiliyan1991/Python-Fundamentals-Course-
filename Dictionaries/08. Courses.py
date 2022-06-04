courses = dict()
info = input()
while info != "end":
    command = info.split(" : ")
    course = command[0]
    name = command[1]
    if course not in courses:
        courses[course] = []
    courses[course].append(name)

    info = input()
for key, value in courses.items():
    print(f"{key}: {len(value)}")

    for i in value:
        print(f"-- {i}")
