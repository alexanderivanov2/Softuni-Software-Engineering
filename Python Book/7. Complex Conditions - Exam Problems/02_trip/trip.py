budget = float(input())
season = input()

budget_spent = 0
destination = ""
place = ""

if budget <= 100:
    if season == "summer":
        budget_spent = budget * 0.30
        destination = "Bulgaria"
        place = "Camp"
    else:
        budget_spent = budget * 0.70
        destination = "Bulgaria"
        place = "Hotel"
elif budget <= 1000:
    if season == "summer":
        budget_spent = budget * 0.40
        destination = "Balkans"
        place = "Camp"
    else:
        budget_spent = budget * 0.80
        destination = "Balkans"
        place = "Hotel"
else:
    budget_spent = budget * 0.90
    destination = "Europe"
    place = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place} - {budget_spent:.2f}")