def line_convert(data_type, line):
    if data_type == "int":
        return int(line) * 2
    elif data_type == "real":
        return f"{float(line) * 1.5:.2f}"
    else:
        return "$" + line + "$"

data_type = input()
line = input()

print(line_convert(data_type, line))