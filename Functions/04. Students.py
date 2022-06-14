text = input()
my_dict = {}
while ":" in text:
    c_info = text.split(":")
    name = c_info[0]
    id = c_info[1]
    course = c_info[2]
    if course not in my_dict:
        my_dict[course] = {}

    my_dict[course][id] = name
    text = input()

text.replace(":", " ")
for id in my_dict[text]:
    print(f"my_dict[info][id] - {id}")
