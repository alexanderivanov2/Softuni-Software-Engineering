first_name = input()
last_name = input()
age = int(input())
town = input()


def concatanate_variables(fn, ln, ages, place_town):
    print(f"You are {fn} {ln}, a {ages}-years old person from {place_town}.")


concatanate_variables(first_name, last_name, age, town)
