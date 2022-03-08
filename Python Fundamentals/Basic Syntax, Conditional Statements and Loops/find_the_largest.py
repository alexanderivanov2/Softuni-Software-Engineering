number = input()
largest_num = sorted([num for num in number], reverse=True)
print("".join(largest_num))