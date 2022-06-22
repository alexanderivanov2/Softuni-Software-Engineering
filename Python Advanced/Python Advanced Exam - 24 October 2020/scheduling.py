numbers = [int(el) for el in input().split(", ")]
index = int(input())

cycles = 0
clocks = numbers[index + 1:] + numbers[:index + 1]
last_cycle = clocks.pop()

for cycle in clocks:
    if cycle <= last_cycle:
        cycles += cycle

print(cycles + last_cycle)