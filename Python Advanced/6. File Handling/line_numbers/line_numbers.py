import re


def count_letters_and_punctuation_marks(line1):
    count_letters = len(re.findall(r"[A-Za-z]", line1))
    count_punctuation_marks = len(re.findall(r'[?!.\-,"\']', line1))
    return f"({count_letters})({count_punctuation_marks})"


def read_text_txt():
    with open("text.txt", "r") as file:
        count = 1
        all_lines = []
        for line in file:
            new_line = f"Line {count}: " + line
            count_tuple = count_letters_and_punctuation_marks(line)
            new_line += " " + count_tuple
            all_lines.append(new_line)
            count += 1
    return '\n'.join(all_lines)


with open("output.txt", "w") as new_file:
    new_file.write(read_text_txt())
