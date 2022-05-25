n = int(input())
best_intersection = []
for _ in range(n):
    command = input().split("-")
    first_range = [int(x) for x in command[0].split(",")]
    second_range = [int(x) for x in command[1].split(",")]
    first_set = set([x for x in range(first_range[0], first_range[1] + 1)])
    second_set = set([x for x in range(second_range[0], second_range[1] + 1)])
    intersection = first_set & second_set

    if len(intersection) > len(best_intersection):
        best_intersection = intersection

print(f"Longest intersection is {''.join(f'{[x for x in best_intersection]}')} with length {len(best_intersection)}"   )
