party_size = int(input())
days = int(input())
total_profit = 0
for i in range(1, days + 1):
    current_day = i
    if current_day % 10 == 0:
        party_size -= 2
    if current_day % 15 == 0:
        party_size += 5

    total_profit += 50 - (2 * party_size)

    if current_day % 3 == 0:
        total_profit -= 3 * party_size
    if current_day % 5 == 0:
        total_profit += 20 * party_size
    if current_day % 3 == 0 and  current_day % 5 == 0:
        total_profit -= 2 * party_size
companion_profit = int(total_profit / party_size)
print(f"{party_size} companions received {companion_profit} coins each.")
