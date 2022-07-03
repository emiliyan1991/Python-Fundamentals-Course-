soft_version = input()
current_soft = list(map(int, soft_version.split(".")))
current_soft[2] += 1
if current_soft[2] == 10:
    current_soft[2] = 0
    current_soft[1] += 1
    if current_soft[1] == 10:
        current_soft[1] = 0
        current_soft[0] += 1


result = list(map(str, current_soft))
print(".".join(result))


