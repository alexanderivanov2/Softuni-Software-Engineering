word = input()

command = input()

while not command == "Finish":
    action, *data = command.split()
    if action == "Replace":
        cur_char = data[0]
        new_char = data[1]
        word = word.replace(cur_char, new_char)
        print(word)
    elif action == "Cut":
        start_index = int(data[0])
        end_index = int(data[1])
        if 0 < start_index < len(word) and 0 < end_index < len(word):
            word = word[:start_index] + word[end_index + 1:]
            #check last?
            print(word)
        else:
            print("Invalid indices!")
    elif action == "Make":
        word = word.upper() if data[0] == "Upper" else word.lower()
        print(word)
    elif action == "Check":
        txt = data[0]
        if txt in word:
            print(f"Message contains {txt}")
        else:
            print(f"Message doesn't contain {txt}")
    elif action == "Sum":
        start_index = int(data[0])
        end_index = int(data[1])
        if 0 < start_index < len(word) and 0 < end_index < len(word):
            sum_word = word[start_index:end_index + 1]
            sum_of_chars = sum([ord(ch) for ch in sum_word])
            print(sum_of_chars)
        else:
            print("Invalid indices!")
    command = input()
