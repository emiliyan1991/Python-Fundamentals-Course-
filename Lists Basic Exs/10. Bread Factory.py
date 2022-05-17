event_string = input().split("|")
energy = 100
coins = 100
diff = 0
bakery_closed = False
for event in event_string:
    current_event = event.split("-")
    command = current_event[0]
    number = int(current_event[1])

    if command == "rest":
        energy += number
        if energy > 100:
            diff = (energy - 100) - number
            energy = 100

            print(f"You gained {diff} energy.")
        else:
            print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")
    elif command == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= number:
            coins -= number
            print(f"You bought {command}.")
        else:
            print(f"Closed! Cannot afford {command}.")
            bakery_closed = True

            break

if not bakery_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")




