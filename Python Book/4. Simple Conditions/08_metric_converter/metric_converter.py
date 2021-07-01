size = float(input())
first_size = input().lower()
second_size = input().lower()
meter = 1
mm = 1000
cm = 100

if first_size == "m":
    result = size / meter
elif first_size == "mm":
    result = size / mm
elif first_size == "cm":
    result = size / cm

if second_size == "m":
    result = result * meter
elif second_size == "mm":
    result = result * mm
elif second_size == "cm":
    result = result * cm

print(f"{result:.3f}")