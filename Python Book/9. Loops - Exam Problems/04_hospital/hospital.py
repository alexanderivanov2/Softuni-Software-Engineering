days = int(input())
doctors = 7
treated = 0
untrated = 0

for i in range(1, days + 1):
    patients = int(input())
    if i % 3 == 0 and untrated > treated:
        doctors += 1

    if patients == doctors:
        treated += doctors
    elif doctors > patients:
        treated += patients
    else:
        treated += doctors
        untrated += patients - doctors

print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untrated}.")