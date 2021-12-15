hrizantemi = int(input())
rose = int(input())
laleta = int(input())
season = input()
is_special = input()
total = 0
if season == "Spring" or season == "Summer":
    hr_price = 2.00
    rose_price = 4.10
    laleta_price = 2.50
    if is_special == "Y":
        hr_price = hr_price + (hr_price * 15 / 100)
        rose_price = rose_price + (rose_price * 15 / 100)
        laleta_price = laleta_price + (laleta_price * 15 / 100)
    total = hrizantemi * hr_price + laleta * laleta_price + rose * rose_price
    if season == "Spring" and laleta > 7:
        total = total - (total * 5 / 100)
    if rose + laleta + hr_price > 20:
        total = total - (total * 20 / 100)
else:
    hr_price = 3.75
    rose_price = 4.50
    laleta_price = 4.15
    if is_special == "Y":
        hr_price = hr_price + (hr_price * 15 / 100)
        rose_price = rose_price + (rose_price * 15 / 100)
        laleta_price = laleta_price + (laleta_price * 15 / 100)
    total = hrizantemi * hr_price + laleta * laleta_price + rose * rose_price
    if season == "Winter" and rose >= 10:
        total = total - (total * 10 / 100)
    if rose + laleta + hr_price > 20:
        total = total - (total * 20 / 100)

print(f"{total + 2:.2f}")