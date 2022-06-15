with open("my_first_file.txt", "w") as file:
    file.write('I just created my first file!')

with open("my_first_file.txt", "r") as file:
    print(file.readlines())