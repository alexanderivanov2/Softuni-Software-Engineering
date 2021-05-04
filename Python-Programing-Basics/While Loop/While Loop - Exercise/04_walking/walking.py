def check_goal(get_steps, get_goals):
    if get_steps < get_goals:
        print(f"{get_goals - get_steps} more steps to reach goal.")
    else:
        print(f"Goal reached! Good job!\n{get_steps - get_goals} steps over the goal!")
    exit()

goal = 10000
steps = 0

while steps < goal:
    steps_make = input()
    if steps_make == "Going home":
        steps += int(input())
        check_goal(steps, goal)
    steps += int(steps_make)

check_goal(steps, goal)
