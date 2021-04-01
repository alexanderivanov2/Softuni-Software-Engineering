budget = float(input())
season = input()
destination = ["Bulgaria", "Balkans", "Europe"]

if budget <= 100:
    place = destination[0]
    if season == "summer":
        budget *= 0.30
        stay_at = "Camp"
    else:
        budget *= 0.70
        stay_at = "Hotel"
elif budget <= 1000:
    place = destination[1]
    if season == "summer":
        budget *= 0.40
        stay_at = "Camp"
    else:
        budget *= 0.80
        stay_at = "Hotel"
else:
    place = destination[2]
    budget *= 0.90
    stay_at = "Hotel"

print(f"Somewhere in {place}")
print(f"{stay_at} - {budget:.2f}")