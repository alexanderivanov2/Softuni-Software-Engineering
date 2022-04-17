electrons = int(input())
cells = 0
n_cells = 1
list_cells = []

while True:
    cell_size = 2 * n_cells ** 2
    if cell_size >= electrons:
        list_cells.append(electrons)
        break
    list_cells.append(cell_size)
    n_cells += 1
    electrons -= cell_size

print(list_cells)
