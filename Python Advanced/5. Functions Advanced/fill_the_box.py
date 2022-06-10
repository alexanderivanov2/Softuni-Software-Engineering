def fill_the_box(h, l, w, *args):
    box = h * l * w
    rest = 0
    for arg in args:
        if arg == "Finish":
            break
        if arg <= box:
            box -= arg
        elif box >= 0:
            rest += arg - box
            box = 0

    if box == 0 and rest > 0:
        return f"No more free space! You have {rest} more cubes."
    return f"There is free space in the box. You could put {box} more cubes."

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
