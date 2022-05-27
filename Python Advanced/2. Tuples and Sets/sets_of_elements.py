n, m = input().split()
n = int(n)
m = int(m)

set_n = set()
set_m = set()

for _ in range(n):
    set_n.add(int(input()))

for _ in range(m):
    set_m.add(int(input()))

unique_elements = set_n.intersection(set_m)

for _ in unique_elements:
    print(_)
