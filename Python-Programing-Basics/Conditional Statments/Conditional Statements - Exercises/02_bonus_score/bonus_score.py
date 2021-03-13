def calculate_bonus_points1(score):
    bonus_points = 0
    if score % 2 == 0:
        bonus_points += 1
    elif score % 10 == 5:
        bonus_points += 2
    bonus_points = calculate_bonus_points2(score, bonus_points)

    print(bonus_points)
    print(score + bonus_points)


def calculate_bonus_points2(score, b_points):
    if score <= 100:
        b_points += 5
    elif score <= 1000:
        b_points += score * 0.20
    elif score > 1000:
        b_points += score * 0.10

    return b_points


points = int(input())
calculate_bonus_points1(points)
