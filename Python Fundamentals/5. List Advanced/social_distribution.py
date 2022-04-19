def find_wealthies(wealthy):
    maximum = max(wealthy)
    count_maximum = wealthy.count(maximum)
    index = wealthy.index(maximum)
    if count_maximum > 1:
        for _ in range(1, count_maximum):
            new_index = wealthy.index(maximum, index + 1)
            index = new_index
    return index


wealthy = [int(n) for n in input().split(", ")]
minimum_wealth = int(input())
do_it = True

for i in range(len(wealthy)):
    if wealthy[i] < minimum_wealth:
        max_index = find_wealthies(wealthy)
        wealth_after_give = wealthy[max_index] - (minimum_wealth - wealthy[i])
        if wealth_after_give < minimum_wealth:
            do_it = False
            break
        need_wealth = minimum_wealth - wealthy[i]
        wealthy[max_index] -= need_wealth
        wealthy[i] += need_wealth
    else:
        break

if do_it:
    print(wealthy)
else:
    print("No equal distribution possible")