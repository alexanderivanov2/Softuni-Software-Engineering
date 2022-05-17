players = {}
players_total = {}

txt = input()
while not txt == "Season end":
    if "->" in txt:
        player, position, skill = txt.split(" -> ")
        skill = int(skill)
        if player not in players:
            players[player] = {position: skill}
            players_total[player] = skill
        elif position not in players[player]:
            players[player][position] = skill
            players_total[player] += skill
        elif players[player][position] < skill:
            players_total[player] -= players[player][position]
            players[player][position] = skill
            players_total[player] += skill
    else:
        player_1, player_2 = txt.split(" vs ")
        if player_1 not in players or player_2 not in players:
            break
        duel = False
        larger = player_1 if len(players[player_1]) >= len(players[player_2]) else player_2
        short = player_2 if larger == player_1 else player_1
        for key, value in players[larger].items():
            if key not in players[short]:
                continue
            elif players_total[larger] == players_total[short]:
                break
            else:
                if players_total[larger] > players_total[short]:
                    del players_total[short]
                    del players[short]
                else:
                    del players_total[larger]
                    del players[larger]
                break
    txt = input()

sort_total = dict(sorted(players_total.items(), key= lambda x: -x[1]))

for key, value in sort_total.items():
    print(f"{key}: {value} skill")
    sort_player = dict(sorted(players[key].items(), key= lambda x: -x[1]))
    for name, skill in sort_player.items():
        print(f"- {name} <::> {skill}")