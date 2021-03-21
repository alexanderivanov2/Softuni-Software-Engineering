number = float(input())
current_metric = input()
convert_metric = input()

if current_metric == "mm":
    if convert_metric == "cm":
        number /= 10
    elif convert_metric == "m":
        number /= 1000
elif current_metric == "cm":
    if convert_metric == "mm":
        number *= 10
    elif convert_metric == "m":
        number /= 100
elif current_metric == "m":
    if convert_metric == "mm":
        number *= 1000
    elif convert_metric == "cm":
        number *= 100

print(f"{number:.3f}")