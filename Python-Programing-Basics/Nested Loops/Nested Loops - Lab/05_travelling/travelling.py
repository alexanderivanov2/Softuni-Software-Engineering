destination = input()
savings = 0

while destination != "End":
    price = float(input())
    while savings < price:
        savings += float(input())
    print(f"Going to {destination}!")
    savings = 0
    destination = input()

