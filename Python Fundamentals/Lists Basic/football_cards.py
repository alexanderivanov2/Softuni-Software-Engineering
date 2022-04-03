team_a = [str(el) for el in range(1, 12)]
team_b = [str(el) for el in range(1, 12)]

cards = [el for el in input().split()]
check = True

for card in cards:
    team, player = card.split("-")
    if team == "A" and player in team_a:
        team_a.remove(player)
    elif team == "B" and player in team_b:
        team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:
        check = False
        break

if check:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
else:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
    print("Game was terminated")