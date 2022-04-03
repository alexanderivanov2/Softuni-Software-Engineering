faro_cards = input().split()
n = int(input())
half = len(faro_cards) // 2
start = faro_cards[0]
end = faro_cards[-1]

for _ in range(n):
    first_half = faro_cards[1:half]
    second_half = faro_cards[half:-1]
    faro_cards = [start]
    for i in range(len(first_half)):
        faro_cards.append(second_half[i])
        faro_cards.append(first_half[i])

    faro_cards.append(end)

print(faro_cards)