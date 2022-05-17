pieces = {}
n = int(input())

for i in range(n):
    piece, composer, key = input().split("|")
    pieces[piece] = {'composer': composer, 'key': key}

command = input()

while not command == "Stop":
    action, *data = command.split("|")
    piece = data[0]
    if action == "Add":
        composer = data[1]
        key = data[2]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {'composer': data[1], 'key': data[2]}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif action == "Remove":
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == "ChangeKey":
        new_key = data[1]
        if piece in pieces:
            pieces[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

sorted_pieces = dict(sorted(pieces.items(), key=lambda x: (x[0], x[1]["composer"])))

for key, value in sorted_pieces.items():
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}")
