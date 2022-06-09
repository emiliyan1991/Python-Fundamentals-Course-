targets = list(map(int, input().split(" ")))
cmd = input()

while cmd != "End":
    command = cmd.split(" ")
    current_command = command[0]
    index = int(command[1])
    value = int(command[2])

    if current_command == "Shoot" and 0 <= index < len(targets):
        targets[index] -= value
        if targets[index] <= 0:
            targets.pop(index)

    elif current_command == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif current_command == "Strike":
        if index - value >= 0 and index + value < len(targets) + 1:
            targets = targets[:index - value] + targets[index+value + 1:]
        else:
            print("Strike missed!")
    cmd = input()
result = list(map(str, targets))
print("|".join(result))


