events = ["coding", "cat", "dog", "movie"]
ENDING = "END"
coffee = 0
event = input()

while not event == ENDING:
    if event.lower() in events:
        coffee += 1
        if event.isupper():
            coffee += 1
    if coffee > 5:
        break
    event = input()

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)
