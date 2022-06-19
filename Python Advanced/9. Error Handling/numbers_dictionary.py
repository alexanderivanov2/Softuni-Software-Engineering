numbers_dictionary = {}

line = input()

while not line == "End":
    if line == "Search":
        searched = input()
        try:
            print(numbers_dictionary[searched])
        except KeyError:
            pass
    elif line == "Remove":
        searched = input()
        try:
            del numbers_dictionary[searched]
        except KeyError:
            print("Number does not exist in dictionary")
    else:
        number_as_string = line
        try:
            number = int(input())
            numbers_dictionary[number_as_string] = number
        except ValueError:
            print("The variable number must be an integer")
    line = input()

print(numbers_dictionary)
