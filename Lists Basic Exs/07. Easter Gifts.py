gift_names = input().split(" ")
index = 0
command1 = input()

last_gift = len(gift_names) - 1
while command1 != "No Money":
    command = command1.split(" ")
    if command[0] == "OutOfStock":
        for gift in gift_names:
            if str(command[1]) in gift:
                gift_names[gift_names.index(gift)] = "None"
    if command[0] == "Required":
        if len(gift_names) >= int(command[2]):
            index = int(command[2])
            gift_names[int(index)] = command[1]
    elif command[0] == "JustInCase":
        gift_names[-1] = command[1]
    command1 = input()
while "None" in gift_names:
    gift_names.remove("None")


print(" ".join(gift_names))






