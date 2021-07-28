name_of_animal = input().lower()

if name_of_animal == "crocodile" or name_of_animal == "tortoise" or name_of_animal == "snake":
    print("reptile")
elif name_of_animal == "dog":
    print("mammal")
else:
    print("unknown")