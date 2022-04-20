num = int(input())
positives = []
negatives = []
negatives_sum = 0
for i in range(num):
    current_num = int(input())
    if current_num >= 0:
        positives.append(current_num)
    else:
        negatives.append(current_num)
        negatives_sum += current_num

print(positives)
print(negatives)

print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {negatives_sum}")
