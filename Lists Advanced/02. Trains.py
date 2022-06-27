number_of_wagons = int(input())
train = [0 for i in range(number_of_wagons)]
command = input()

while command != "End":
    explode = command.split(" ")
    current = explode[0]
    if current == "add":
        num_people = int(explode[1])
        train[-1] += num_people
    elif current == "insert":
        num_people = int(explode[2])
        position = int(explode[1])
        train[position] += num_people
    elif current == "leave":
        num_people = int(explode[2])
        position = int(explode[1])
        train[position] -= num_people
    command = input()

print(train)