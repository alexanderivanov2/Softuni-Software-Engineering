txt = input().split('\\')

file_name, file_extension = txt[-1].split(".")
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")