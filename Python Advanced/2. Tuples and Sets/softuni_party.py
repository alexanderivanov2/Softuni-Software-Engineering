n = int(input())
guests = set()
guest = input()

while guest != "END":
    if guest not in guests:
        guests.add(guest)
    else:
        guests.remove(guest)
    guest = input()

guests = sorted(guests, key=lambda x: x)
print(len(guests))
print("\n".join(guests))
