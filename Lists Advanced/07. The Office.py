employees = list(map(int, input().split(" ")))
factor = int(input())
filtered = [filter(lambda x: x >= (sum(employees) / len(employees)), employees)]
if len(filtered) >= len(employees) / 2:
    print(f"Score: {factor}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {factor}/{len(employees)}. Employees are not happy!")
