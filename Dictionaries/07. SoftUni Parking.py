park_dict = {}
cars_in = int(input())
for car in range (cars_in):
    info = input().split(" ")
    command = info[0]
    name = info[1]

    if command == "register":
        id = info[2]
        if name not in park_dict:
            park_dict[name] = id
            print(f"{name} registered {id} successfully")
        else:
            print(f"ERROR: already registered with plate number {id}")
    elif command == "unregister":
        if name not in park_dict:
            print(f"ERROR: user {name} not found")
        else:
            park_dict.pop(name)

            print(f"{name} unregistered successfully")

for key, value in park_dict.items():
    print(f"{key} => {value}")
