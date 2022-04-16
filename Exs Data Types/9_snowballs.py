
snowball_number = int(input())

best_weight = 0
best_time = 0
best_quality = 0
best_result = 0

for i in range(1, snowball_number + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())
    result = (weight / time) ** quality
    if result > best_result:
        best_result = result
        best_weight = weight
        best_time = time
        best_quality = quality

print(f"{best_weight} : {best_time} = {best_result:.0f} ({best_quality})")



