text = input()
occurrences = {}

for i in text:
    if i != " ":
        if i not in occurrences:
            occurrences[i] = 1
        else:
            occurrences[i] += 1

for key, value in occurrences.items():
    print(f"{key} -> {value}")


