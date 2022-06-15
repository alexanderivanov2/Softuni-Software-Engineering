from collections import deque


def convert_line(lines):
    symbols = ["-", ",", ".", "!", "?"]
    reversed_line = deque()
    for word in lines:
        convert_word = ''.join(["@" if el in symbols else el for el in word])
        reversed_line.appendleft(convert_word)
    return " ".join(reversed_line)


def get_lines_and_convert():
    with open('text.txt', "r") as file:
        count = 0
        for line in file:
            if count % 2 == 0:
                current_line = line.split()
                current_line = convert_line(current_line)
                print(current_line)
            count += 1


get_lines_and_convert()
