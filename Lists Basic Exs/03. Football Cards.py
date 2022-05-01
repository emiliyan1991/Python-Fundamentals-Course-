cards_given = input().split(" ")

a_team_count = 11
b_team_count = 11
game_terminated = False
cards = []

for card in cards_given:
    if card not in cards:
        cards.append(card)
        if "A" in card:
            a_team_count -= 1
        elif "B" in card:
            b_team_count -= 1
        if a_team_count < 7 or b_team_count < 7:
            game_terminated = True
            break
print(f"Team A - {a_team_count}; Team B - {b_team_count}")
if game_terminated:
    print("Game was terminated")


