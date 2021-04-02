month = input()
nights = int(input())
may_oct = ["May", "October"]
jun_sep = ["June", "September"]

if month in may_oct:
    studio = 50 * nights
    apartment = 65 * nights
    if nights > 14:
        studio *= 0.70
        apartment *= 0.90
    elif nights > 7:
        studio *= 0.95
elif month in jun_sep:
    studio = 75.20 * nights
    apartment = 68.70 * nights
    if nights > 14:
        studio *= 0.80
        apartment *= 0.90
else:
    studio = 76 * nights
    apartment = 77 * nights
    if nights > 14:
        apartment *= 0.90


print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")
