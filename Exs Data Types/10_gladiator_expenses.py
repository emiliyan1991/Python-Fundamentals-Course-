lost_fight_count = int(input())
helmet_repair = float(input())
sword_repair = float(input())
shield_repair = float(input())
armor_repair = float(input())
shield_break_counter = 0
expenses = 0

for day in range(1,lost_fight_count + 1):
    if day % 2 == 0:
        expenses += helmet_repair
    if day % 3 == 0:
        expenses += sword_repair
    if day % 2 == 0 and day % 3 == 0:
        expenses += shield_repair
        shield_break_counter += 1
        if shield_break_counter % 2 == 0 and shield_break_counter > 0:
            expenses += armor_repair

print(f"Gladiator expenses: {expenses:.2f} aureus")
