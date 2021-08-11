season = input().lower()
nights = int(input())

studio = 0
apartment = 0

if season == "may" or season == "october":
    studio = 50 * nights
    apartment = 65 * nights
    if 7 < nights <= 14:
        studio = studio - (studio * 0.05)
    elif nights > 14:
        studio = studio - (studio * 0.30)
        apartment = apartment - (apartment * 0.1)
elif season == "june" or season == "september":
    studio = 75.20 * nights
    apartment = 68.70 * nights
    if nights > 14:
        studio = studio - (studio * 0.2)
        apartment = apartment - (apartment * 0.1)
else:
    studio = 76 * nights
    apartment = 77 * nights
    if nights > 14:
        apartment = apartment - (apartment * 0.1)

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")